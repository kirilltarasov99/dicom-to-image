import numpy as np
from PIL import Image


test = np.load('NCMBP0G2.npy')
filepath = 'test/NCMBP0G2.npy'
print(test[0])
print(test[0].shape)
for frame in range(3):
    img = test[frame]
    im = Image.fromarray(img, 'L')
    savename = [filepath, str(frame), '.jpg']
    im.save('_'.join(savename))
