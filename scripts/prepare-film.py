from pathlib import Path
import subprocess,json
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
film=root/'assets/landing-film.mp4'
for name,width in [('desktop',1440),('mobile',960)]:
 out=root/'assets/film'/name;out.mkdir(parents=True,exist_ok=True)
 subprocess.run(['ffmpeg','-v','error','-i',str(film),'-vf',f'fps=24,scale={width}:-2','-start_number','0','-y',str(out/'%03d.png')],check=True)
 for f in sorted(out.glob('*.png')):
  Image.open(f).save(f.with_suffix('.webp'),quality=76);f.unlink()
frames=sorted((root/'assets/film/desktop').glob('*.webp'))
(root/'assets/film/manifest.json').write_text(json.dumps({'count':len(frames),'fps':24,'duration':8}))
Image.open(frames[0]).save(root/'assets/film-poster.webp',quality=90)
board=Image.new('RGB',(1200,810),'white');draw=ImageDraw.Draw(board)
for i in range(9):
 n=round(i*(len(frames)-1)/8);im=Image.open(frames[n]);im.thumbnail((400,240));x=i%3*400;y=i//3*270;board.paste(im,(x,y));draw.text((x+8,y+240),f'Frame {n} / {n/24:.2f}s',fill='black')
board.save(root/'review/film-contact-sheet.jpg')
print('Prepared',len(frames),'frames for each viewport')
