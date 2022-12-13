from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
new_astro = img.resize((400,200))
thumbnail_astro = img
thumbnail_astro.thumbnail((400,200))
new_astro.save('new-astro.jpg')
thumbnail_astro.save('astro-thumbnail.jpg')


new_astro.show()
thumbnail_astro.show()

print(thumbnail_astro.size)