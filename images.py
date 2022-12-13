from PIL import Image

img = Image.open('./pokedex/Boba Fett.jpg')

box = (150,150,300,300)

bobafett_BandW = img.convert('L')
bobafett_BandW.save()