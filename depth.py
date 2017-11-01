import cv2
import utils
import numpy

# Devices.CAP_OPENNI = 900 # OpenNI (for Microsoft
# Kinect)CAP_OPENNI_ASUS = 910 # OpenNI (for Asus Xtion)

# Channels of an OpenNI-compatible depth
#    generator.CAP_OPENNI_DEPTH_MAP = 0 # Depth values in mm
#       (16UC1)CAP_OPENNI_POINT_CLOUD_MAP = 1 # XYZ in meters
#           (32FC3)CAP_OPENNI_DISPARITY_MAP = 2 # Disparity in
#               pixels (8UC1)CAP_OPENNI_DISPARITY_MAP_32F = 3 #
#                   Disparity in pixels
#                       (32FC1)CAP_OPENNI_VALID_DEPTH_MASK = 4 #
#                           8UC1
# Channels of an OpenNI-compatible RGB image
# generator.CAP_OPENNI_BGR_IMAGE = 5CAP_OPENNI_GRAY IMAGE = 6

def createMedianMask(disparityMap, validDepthMask, rect = None):
    """Return a mask selecting the median layer, plus shadows."""
    if rect is not None:
        x, y, w, h = rect
        disparityMap = disparityMap[y:y+h, x:x+w]
        validDepthMask = validDepthMask[y:y+h, x:x+w]
    median = numpy.median(disparityMap)

    return numpy.where((validDepthMask == 0) | \
                       (abs(disparityMap - median) < 12),
                       1.0, 0.0)