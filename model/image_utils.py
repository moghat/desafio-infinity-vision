from numpy import ndarray
import cv2
import sys

def load_img(img_path: str) -> ndarray:
    '''Load and return image in ndarray.'''
    try:
        img = cv2.imread(img_path)
    except Exception as e:
        print("An Error occured during image file load:", e)
        sys.exit(0)

    return img
    
def pre_process_img(img: ndarray) -> ndarray:
    '''Returns input image converted to grayscale and resized to 256x256'''
    ## Convert BGR to Graysacle
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ## Resize TO 256x256 
    img_gray_res = cv2.resize(img_gray, [256,256])
    
    return img_gray_res

def read_image(img_path: str) -> ndarray:
    ## Load image
    img = load_img(img_path)
    ## Pre process image
    img_pp = pre_process_img(img)

    return img_pp