import imageio
import scipy as np


im = imageio.imread('Image_ecam.jpg')
print(np.reshape(im,(225,3,225)))

def transfo_rouge(im):
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]          # déballe les valeurs RGB de chaque pixel
            if r < 100 :                # Ici je regarde si R est petit, puis que ECAM est en Bleu, R est faible 
                im[i, j] = (255, 0,0)          # Je remplace le pixel bleu (ici il n'a qu'eux qui ont un r faible) par un pixel rouge          
    return im

transfo_rouge(im)
# im = im.reshape(135,375,3)                permet de changer la forme, réorganise les pixels. 3 doit rester car RGB le reste doit former le même nbre de pixels qu'avant 225x225
imageio.imwrite('Image-ecam-transformed.jpg', im.astype(np.uint8))
