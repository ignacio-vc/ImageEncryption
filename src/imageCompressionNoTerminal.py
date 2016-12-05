from _future_ import division
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#%matplotlib inline

image = np.array(Image.open(Test.png))

image = image / 255

row,col,_ = image.shape

print("pixels: ",row,"*",col)

fig = plt.figure(figsize=(15,10))
a = fig.add.subplot(1,1,1)
imgplot = plt.imshow(image)
a.set.title("Algo")
plt.show()


