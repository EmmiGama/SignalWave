from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt


def main():
  name = 'interface'

  img = Image.open(f'./{name}.png')

  arr = np.asarray(ImageOps.grayscale(img))
  arr = np.flipud(arr)
  
  arr = np.where(arr < 1, arr, 1)

  plt.pcolormesh(arr)
  plt.show()

  with open(f'{name}.txt', 'w') as f:
    f.write('[')

    for j, y in enumerate(arr):
      f.write('[')
      for i, x in enumerate(y):

        f.write(f'{x}')

        if i != (len(y) - 1):
          f.write(', ')

      f.write(']')

      if j != (len(arr) - 1):
        f.write(', \n')

    f.write(']')
      


if __name__ == '__main__':
  main()