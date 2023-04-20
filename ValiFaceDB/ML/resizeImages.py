import cv2
import os
import numpy as np

#This module resizes image from a given directory to 100*100 pixels and writes all images to given directory
def resizeImages(directory): 
  count=0
  for path, subdirnames, filenames in os.walk(directory):
      for filename in filenames:
        if filename.startswith("."):
          print("Skipping File:",filename)#Skipping files that startwith .
          continue
        img_path=os.path.join(path, filename)#fetching image path
        print("img_path",img_path)
        id=os.path.basename(path)#fetching subdirectory names
        img = cv2.imread(img_path)
        if img is None:
          print("Image not loaded properly")
          continue
        resized_image = cv2.resize(img, (100, 100))
        new_path="resizedTrainingImages"+"/"+str(id)
        if(os.path.exists(new_path)): 
          print("desired path is",os.path.join(new_path, "frame%d.jpg" % count))#write all images to resizedTrainingImages/id directory
          cv2.imwrite(os.path.join(new_path, "frame%d.jpg" % count),resized_image)
        else:
          os.makedirs(new_path)
          print("new directory made: ",os.path.join(new_path))#make a new directory and writes the image to the new path
          cv2.imwrite(os.path.join(new_path, "frame%d.jpg" % count),resized_image)
        count += 1
