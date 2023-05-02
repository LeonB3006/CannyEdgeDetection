import cv2
import numpy
from Detectors.DetectorABC import DetectorABC


class CannyDet(DetectorABC):

    def __init__(self, lower_threshold, upper_threshold, arp_size=3):
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold
        self.arp_size = arp_size


    def detect(self, img_path):
        print("Detecting!!!")
        image = cv2.imread(img_path)
        image_edges = cv2.Canny(image, self.lower_threshold, self.upper_threshold)
        self.print_image(image, image_edges)



