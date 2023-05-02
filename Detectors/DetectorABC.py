from abc import ABC, abstractmethod
import cv2
class DetectorABC(ABC):

    @abstractmethod
    def detect(self, img_path):
        pass


    def print_image(self, image, image_edges):
        cv2.imshow('Original',image)
        cv2.imshow('Edges Detected', image_edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
