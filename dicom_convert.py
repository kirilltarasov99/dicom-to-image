import pydicom as dicom
import sys
import cv2
import numpy as np


filepath = sys.argv[1]
ds = dicom.dcmread(filepath)
format = sys.argv[2]
if len(sys.argv) > 3:
    with open(sys.argv[3], 'r') as file:
        lines = file.readlines()
    x_low = int(lines[0])
    x_high = int(lines[1])
    y_low = int(lines[2])
    y_high = int(lines[3])
    pixel_array_numpy = ds.pixel_array[:, x_low:x_high, y_low:y_high, :]
else:
    pixel_array_numpy = ds.pixel_array

match format:
    case 'jpg':
        for frame in range(pixel_array_numpy[0]):
            img = pixel_array_numpy[frame]
            savename = [filepath, str(frame), '.jpg']
            cv2.imwrite('_'.join(savename), cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR))

    case 'npy':
        converted_list = []
        for frame in pixel_array_numpy:
            img = frame
            converted_image_data = cv2.cvtColor(frame, cv2.COLOR_YCrCb2BGR)
            converted_list.append(cv2.cvtColor(converted_image_data, cv2.COLOR_BGR2GRAY))
        np.save(filepath, np.array(converted_list))

    case 'png':
        for frame in range(pixel_array_numpy.shape[0]):
            img = pixel_array_numpy[frame]
            savename = [filepath, str(frame), '.png']
            cv2.imwrite('_'.join(savename), cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR))

