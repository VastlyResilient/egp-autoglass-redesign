"""Prepared image-guided request. Dry-run default; submit only after one-job approval."""
import argparse,importlib.util,json,ssl,certifi,time,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ssl._create_default_https_context=lambda:ssl.create_default_context(cafile=certifi.where())
s=importlib.util.spec_from_file_location('owner_video','/Users/bobby/codex-video-gen/gen_video.py')
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
p=argparse.ArgumentParser();p.add_argument('--submit-approved',action='store_true');a=p.parse_args()
model=next(m for m in v.api('/videos/models')['data'] if m['id']=='google/veo-3.1-fast')
assert 'first_frame' in model['supported_frame_images'] and 8 in model['supported_durations'] and '1080p' in model['supported_resolutions']
payload=dict(model=model['id'],prompt=(ROOT/'research/install-guided-prompt.txt').read_text(),duration=8,resolution='1080p',aspect_ratio='16:9',generate_audio=True,frame_images=[dict(type='image_url',image_url=dict(url='https://vastlyresilient.github.io/egp-autoglass-redesign/assets/install-keyframe-v3.png'),frame_type='first_frame')])
(ROOT/'research/install-guided-payload.json').write_text(json.dumps(payload,indent=2))
print('Estimated cost $'+str(8*float(model['pricing_skus']['duration_seconds_with_audio'])))
if not a.submit_approved:
 print('DRY RUN: no submission. Exact payload saved in research/install-guided-payload.json');raise SystemExit()
receipt=ROOT/'research/install-guided-job.json'
if receipt.exists():raise SystemExit('Existing job record: refuse duplicate submission. Poll existing job separately.')
r=v.api('/videos',payload);receipt.write_text(json.dumps(r,indent=2));print('Submitted once:',r['id'],flush=True)
while True:
 r=v.api('/videos/'+r['id']);status=r['status'];print(status,flush=True)
 if status=='completed':break
 if status in ('failed','cancelled','expired'):raise SystemExit('Job stopped. No retry authorized.')
 time.sleep(15)
clean={k:x for k,x in r.items() if k not in ('urls','unsigned_urls')};receipt.write_text(json.dumps(clean,indent=2))
req=urllib.request.Request(r['unsigned_urls'][0],headers={'Authorization':'Bearer '+v.KEY})
with urllib.request.urlopen(req,timeout=300) as response,(ROOT/'assets/install-guided-v3.mp4').open('wb') as out:out.write(response.read())
print('Downloaded. Actual cost:',r.get('usage',{}).get('cost'))
