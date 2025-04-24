import numpy as np
from keras.models import load_model

import cv2

import numpy
from PIL import Image, ImageFilter 


imgpath='Input Testing Images/cr4.jpg'

def initDetection(imgpath):
    from keras.preprocessing import image
    
    mymodel=load_model('model/crackmodel.h5')      
    test_image=image.load_img(imgpath,target_size=(227,227,3))
    test_image=image.img_to_array(test_image)
    test_image=np.expand_dims(test_image,axis=0)
    pred=mymodel.predict(test_image)[0][0]
    print("Prediction score ",pred)
    if pred==0:
        imageob = Image.open(imgpath).convert('RGB')
        imageob = imageob.filter(ImageFilter.FIND_EDGES)
        imageob.save("tempimage.jpg")
        
        print("CRACK")
        image = cv2.imread(imgpath)
        window_name = 'CRACK'
        ims=cv2.resize(image,(350,350))
        cv2.imshow(window_name, ims)
       # cv2.waitKey(0) 
       # cv2.destroyAllWindows() 
        
        image1 = cv2.imread("tempimage.jpg")
        sam = 'CRACKS MARKED'
        ims1=cv2.resize(image1,(350,350))
        cv2.imshow(sam, ims1)
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 
        
    else:
        print("NON CRACK")
        image = cv2.imread(imgpath)
        window_name = 'NO CRACK'
        ims=cv2.resize(image,(350,350))
        cv2.imshow(window_name, ims)
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 