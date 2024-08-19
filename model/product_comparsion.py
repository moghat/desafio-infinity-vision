from model.yaml_utils import read_yaml
from model.image_utils import read_image

import numpy as np
import cv2
from scipy.spatial.distance import cosine
from typing import List

def get_graysacle_histogram(img: np.ndarray) -> List[int]:
        '''Returns histogram of a gray scale image'''
        ## Calculate the histogram of input image
        hist = cv2.calcHist([img], [], None, [256], [0, 256])
        ## Organize values in a list of int
        histogram = [int(a) for a in hist]
        return histogram


class ProdructComparison():
    def __init__(self, yaml_path) -> None:
        self.comp_param = read_yaml(yaml_path)
        self.img_a = read_image(self.comp_param.image_a)
        self.img_b = read_image(self.comp_param.image_b)

    def compare(self):
        '''Makes the comparison bewtween the images and display the result in the terminal'''

        ## Gets the grayscale histogram of each image
        hist_a = get_graysacle_histogram(self.img_a)
        hist_b = get_graysacle_histogram(self.img_b)

        ## Calculate the angular distance between the histograms
        ang_distance = self.__calculate_angular_distance(hist_a, hist_b)
        ## Display result
        self.__comparison_result(ang_distance, self.comp_param.threshold)

        ## Save images in single image sticked side by side
        self.__save_images()
    
    def __calculate_angular_distance(self, hist_a: List[int], hist_b: List[int]) -> np.float64:
        '''Returns angular distance between the 2 input 1D histograms'''
        result = cosine(hist_a, hist_b)

        return result
    
    def __comparison_result(self, distance_value: np.float64, thresh: float) -> None:
        '''Display the results of the products comparison, incluiding the distance value.'''
        
        print('distância:', distance_value)
        
        if distance_value <= thresh:
            print("Mesmo produto")
        else:
            print("Produtos diferentes")

    def __save_images(self) -> None:
        ## Stick the 2 images together side by side
        sideBySide_images = np.concatenate((self.img_a, self.img_a), axis=1)
        ## Save the side by side image in the output_location parameter
        cv2.imwrite(self.comp_param.output_location, sideBySide_images)

