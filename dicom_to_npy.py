import pydicom as dicom
import sys
import cv2
import numpy as np


filepath = sys.argv[1]
ds = dicom.dcmread(filepath)
pixel_array_numpy = ds.pixel_array

converted_list = []
for frame in pixel_array_numpy:
    converted_image_data = cv2.cvtColor(frame, cv2.COLOR_YCrCb2BGR)
    converted_list.append(cv2.cvtColor(converted_image_data, cv2.COLOR_BGR2GRAY))
np.save(filepath, np.array(converted_list))
