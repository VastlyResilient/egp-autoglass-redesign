"""Prepared image-guided request. Dry-run default; submit only after one-job approval."""
import argparse,importlib.util,json,ssl,certifi,time,urllib.request,urllib.error,hashlib,io
from PIL import Image
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ssl._create_default_https_context=lambda:ssl.create_default_context(cafile=certifi.where())
s=importlib.util.spec_from_file_location('owner_video','/Users/bobby/codex-video-gen/gen_video.py')
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
p=argparse.ArgumentParser();p.add_argument('--submit-approved',action='store_true');a=p.parse_args()
model=next(m for m in v.api('/videos/models')['data'] if m['id']=='google/veo-3.1-fast')
assert 'first_frame' in model['supported_frame_images'] and 8 in model['supported_durations'] and '1080p' in model['supported_resolutions']
payload=dict(model=model['id'],prompt=(ROOT/'research/install-guided-v4-prompt.txt').read_text(),duration=8,resolution='1080p',aspect_ratio='16:9',generate_audio=True,frame_images=[dict(type='image_url',image_url=dict(url='https://vastlyresilient.github.io/egp-autoglass-redesign/assets/install-keyframe-v3.png'),frame_type='first_frame')])
(ROOT/'research/install-guided-v4-payload.json').write_text(json.dumps(payload,indent=2))
assert 'last_frame' in model['supported_frame_images']
revision=(ROOT/'research/install-v4-asset-revision.txt').read_text().strip()
payload['frame_images']=[]
for role,name in [('first_frame','install-keyframe-v3.png'),('last_frame','install-end-v4-clean.png')]:
 url=f'https://raw.githubusercontent.com/VastlyResilient/egp-autoglass-redesign/{revision}/assets/{name}'
 with urllib.request.urlopen(url,timeout=30) as response:
  assert response.status==200, 'Starting or ending image unavailable'
  image_bytes=response.read()
 assert hashlib.sha256(image_bytes).digest()==hashlib.sha256((ROOT/'assets'/name).read_bytes()).digest(), 'Published image differs from inspected image'
 with Image.open(io.BytesIO(image_bytes)) as im: im.verify()
 payload['frame_images'].append(dict(type='image_url',image_url=dict(url=url),frame_type=role))
(ROOT/'research/install-guided-v4-payload.json').write_text(json.dumps(payload,indent=2))
print('Preflight passed: both immutable published frames match inspected local files.')
assert 8*float(model['pricing_skus']['duration_seconds_with_audio']) <= 0.96, 'Cost exceeds authorized cap'
print('Estimated cost $'+str(8*float(model['pricing_skus']['duration_seconds_with_audio'])))
if not a.submit_approved:
 print('DRY RUN: no submission. Exact payload saved in research/install-guided-v4-payload.json');raise SystemExit()
receipt=ROOT/'research/install-guided-v4-job.json'
if receipt.exists():raise SystemExit('Existing job record: refuse duplicate submission. Poll existing job separately.')
attempt=ROOT/'research/install-guided-v4-attempt.json'
if attempt.exists():raise SystemExit('Prior attempt exists. A new explicit approval and separately recorded attempt are required.')
attempt.write_text(json.dumps({'state':'submission_started','time':time.time()},indent=2))
try:
 r=v.api('/videos',payload)
except urllib.error.HTTPError as error:
 body=error.read().decode('utf-8',errors='replace').replace(v.KEY,'[REDACTED]')
 attempt.write_text(json.dumps({'state':'http_error','status':error.code,'response':body},indent=2))
 raise SystemExit('Submission rejected; diagnostics saved. No automatic retry.')
receipt.write_text(json.dumps(r,indent=2));print('Submitted once:',r['id'],flush=True)
while True:
 r=v.api('/videos/'+r['id']);status=r['status'];print(status,flush=True)
 if status=='completed':break
 if status in ('failed','cancelled','expired'):raise SystemExit('Job stopped. No retry authorized.')
 time.sleep(15)
clean={k:x for k,x in r.items() if k not in ('urls','unsigned_urls')};receipt.write_text(json.dumps(clean,indent=2))
req=urllib.request.Request(r['unsigned_urls'][0],headers={'Authorization':'Bearer '+v.KEY})
with urllib.request.urlopen(req,timeout=300) as response,(ROOT/'assets/install-guided-v4.mp4').open('wb') as out:out.write(response.read())
print('Downloaded. Actual cost:',r.get('usage',{}).get('cost'))
