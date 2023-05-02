from Detectors.Canny.CannyDet import CannyDet
from Detectors.Laplace.LaplaceDet import LaplaceDet


def main():
    my_canny_detector = CannyDet(50, 150, 7)
    my_canny_detector.detect("img/test_img_02.jpg")

    my_laplace_detector = LaplaceDet()
    my_laplace_detector.detect("img/test_img_02.jpg")#



main()