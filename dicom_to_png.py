import pydicom as dicom
import sys
from PIL import Image


filepath = sys.argv[1]
ds = dicom.dcmread(filepath)
pixel_array_numpy = ds.pixel_array

for frame in range(pixel_array_numpy.shape[0]):
    img = pixel_array_numpy[frame]
    im = Image.fromarray(img, 'YCbCr')
    savename = [filepath, str(frame), '.jpg']
    im.save('_'.join(savename))

