import numpy as np
import skimage
import matplotlib.pyplot as plt
from skimage.io import imread

!wget -O imagen_examen.jpg https://i.ibb.co/mNcvWF8/pregunta2-examen4.jpg #si no funciona es porque el enlace caduco, en ese caso solo se descargo desde el ordenador
im = imread('imagen_examen.jpg')#descargue el archivo, lo subio a mi colab con este nombre
canti = im.shape

plt.imshow(im)
