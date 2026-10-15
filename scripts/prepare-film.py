"""Prepare scroll frames only from a reviewed source; never default to old footage."""
from pathlib import Path
import argparse, hashlib, json, subprocess, tempfile
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ('story','causality','contact','anatomy','identity','geometry','lighting','artifacts','ending','desktop_crop','mobile_crop')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--review', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True, help='New, non-existing staging directory; does not change live assets')
    args = parser.parse_args()
    staging_root = (ROOT/'review'/'film-staging').resolve()
    args.output = args.output.resolve()
    if staging_root not in args.output.parents:
        parser.error('Output must be a new directory below review/film-staging; live asset paths are prohibited.')
    review = json.loads(args.review.read_text())
    if review.get('status') != 'accepted':
        parser.error('Film review is not accepted. No frames written.')
    film = Path(review.get('clip',''))
    if not film.is_file() or hashlib.sha256(film.read_bytes()).hexdigest() != review.get('sha256'):
        parser.error('Reviewed clip missing or changed. No frames written.')
    for key in CHECKS:
        check = review.get('checks',{}).get(key,{})
        if check.get('result') != 'pass' or not check.get('finding'):
            parser.error('Missing or failed review check: '+key)
    if not review.get('events') or not review.get('evidence') or any(not Path(p).is_file() for p in review['evidence']):
        parser.error('Missing event or inspection evidence.')
    if args.output.exists():
        parser.error('Output already exists; preserve it and choose a new staging directory.')
    metadata = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(film)]))
    duration = float(metadata['format']['duration'])
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=args.output.parent) as tmp:
        stage = Path(tmp)/'frames'; stage.mkdir()
        for name,width in [('desktop',1440),('mobile',960)]:
            out=stage/name;out.mkdir()
            subprocess.run(['ffmpeg','-v','error','-i',str(film),'-vf',f'fps=24,scale={width}:-2','-start_number','0',str(out/'%03d.png')],check=True)
            for f in sorted(out.glob('*.png')):
                with Image.open(f) as im: im.save(f.with_suffix('.webp'),quality=76)
                f.unlink()
        frames=sorted((stage/'desktop').glob('*.webp'))
        if not frames or len(frames)!=len(list((stage/'mobile').glob('*.webp'))):
            raise RuntimeError('Incomplete desktop/mobile sequence')
        (stage/'manifest.json').write_text(json.dumps({'count':len(frames),'fps':24,'duration':duration,'source_sha256':review['sha256']},indent=2))
        with Image.open(frames[0]) as im: im.save(stage/'poster.webp',quality=90)
        board=Image.new('RGB',(1200,810),'white');draw=ImageDraw.Draw(board)
        for i in range(9):
            n=round(i*(len(frames)-1)/8)
            with Image.open(frames[n]) as im:
                im.thumbnail((400,240));x=i%3*400;y=i//3*270;board.paste(im,(x,y))
                draw.text((x+8,y+240),f'Frame {n} / {n/24:.2f}s',fill='black')
        board.save(stage/'contact-sheet.jpg')
        stage.rename(args.output)
    print(f'Prepared {len(frames)} frames per viewport in {args.output}. Live website unchanged.')

if __name__=='__main__': main()
