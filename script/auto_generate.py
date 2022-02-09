from PIL import Image
import os

ORIGIN_CRAPE_PATH = 'origin_cutoff'

TEMPLATE = 'PixelSpace.gif'
CRAPE_RESIZE = (330, 330)
CRAPE_POSITION_ON_TEMPLATE = (80, 30)
OUTPUT_PATH = 'Pixel_Space'

files = os.listdir(ORIGIN_CRAPE_PATH)
files.sort(key=lambda x: x[:-4])

template_img = Image.open(TEMPLATE)

if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

for file in files:
    crape_img = Image.open(ORIGIN_CRAPE_PATH+'/'+file)
    crape_img = crape_img.resize(CRAPE_RESIZE).convert('RGBA').copy()
    # crape_img.show()
    images = []
    for frame in range(0, template_img.n_frames):
        template_img.seek(frame)
        tmp_img = template_img.convert('RGBA').copy()
        tmp_img.paste(crape_img, CRAPE_POSITION_ON_TEMPLATE, crape_img)
        images.append(tmp_img.copy())
    images[0].save(OUTPUT_PATH+'/'+file.split('.')[0] +'.gif', save_all=True, append_images=images[1:], optimize=False, duration=10, loop=0)
    # break
