import os
import cv2
import time
def imageScaling(inputpath,scaledpath):
  
    for path in os.listdir(inputpath):
       
        image_path = os.path.join(inputpath, path)
        if os.path.isfile(image_path):
            image = cv2.imread(image_path)
            dim = (227, 227)
           
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            fn=path.split(".")
            fname=fn[0]
          #  print(fname)
            newfilepath=scaledpath+"//"+fname+".jpg"
            cv2.imwrite(newfilepath, resized) 
          #  print(newfilepath," stored")
                        

            
        
      
        
inputpath = "dataset/train/crack"     
st = time.time()
imageScaling(inputpath,inputpath)
et = time.time()
elapsed_time = et - st
print('Resizing Execution time:', elapsed_time, 'seconds')


#print('Process is Completed.... Please  view '+newdirpath+" and "+ newroipath+" for Resulted Images")
