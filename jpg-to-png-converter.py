from PIL import Image, ImageFilter
import sys
import os


pokedex = sys.argv[1]
png_pokedex = sys.argv[2]


if not os.path.exists(png_pokedex):
    os.makedirs(png_pokedex)
    

for filename in os.listdir(pokedex):
  img = Image.open(f'{pokedex}{filename}')
  clean_name = os.path.splitext(filename)[0]
  img.save(f'{png_pokedex}/{clean_name}.png')
  print('all done!')