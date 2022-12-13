from PIL import Image, ImageFilter

img = Image.open('./pokedex/squirtle.jpg')

gray = img.convert('L')
filtered_gray = gray.filter(ImageFilter.BLUR)
filtered_gray.save('filtered-gray.png')

filtered_gray.show()