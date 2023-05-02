import cv2

from Detectors.DetectorABC import DetectorABC


class LaplaceDet(DetectorABC):
    def __init__(self):
        pass

    def detect(self, img_path):
        image = cv2.imread(img_path)
        image_edges = cv2.Laplacian(image, cv2.CV_64F)
        self.print_image(image, image_edges)

