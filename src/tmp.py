import heightmap
import numpy
from PIL import Image

tmp = (255 * heightmap.HeightMap(10)).astype(int)

img = Image.new('RGB', (2**9+1, 2**10+1), color='red')
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = tuple([tmp[i][j]]*3)

img.show()
