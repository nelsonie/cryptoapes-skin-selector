from PIL import Image
import os
import json

ORIGIN_CRAPE_PATH = 'origin'

CRAPE_PROPERTIES_PATH = 'ape_properties'
TEMPLATE_PATH = 'wallpaper_template'
CRAPE_RESIZE = (1200, 1200)
CRAPE_POSITION_ON_TEMPLATE = (0, 1350)
OUTPUT_PATH = 'Solavirus_Wallpaper'

files = os.listdir(ORIGIN_CRAPE_PATH)
files.sort(key=lambda x: x[:-4])

template_map = {}
for template in os.listdir(TEMPLATE_PATH):
    template_img = Image.open(TEMPLATE_PATH + '/' + template)
    template_map[template.split('.')[0]] = template_img


def get_template_img(crape_id):
    with open(CRAPE_PROPERTIES_PATH + '/' + crape_id + '.json') as fh:
        j = json.loads(fh.read())
        return template_map[j['attributes'][0]['value']]


if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)


for file in files:
    crape_img = Image.open(ORIGIN_CRAPE_PATH+'/'+file)
    crape_img = crape_img.resize(CRAPE_RESIZE).convert('RGBA').copy()
    # crape_img.show()
    tmp_img = get_template_img(file.split('.')[0]).copy()
    tmp_img.paste(crape_img, CRAPE_POSITION_ON_TEMPLATE, crape_img)
    tmp_img.save(OUTPUT_PATH+'/'+file.split('.')[0] +'.png')
    # break
