from __future__ import division    #neccesary for cv2
import numpy as np    #neccesary for cv2
import cv2
import camera_m as camera
from camera_m import removearray as remove_a   #because of a bug we need a function for sorting through arrays
import geogebra_m as geo

camera0 = camera.setup(320,240) #width,height

sliderstart = (0, 0, 0, 255, 255, 255)   #staring values for sliders
camera.setup_sliders(sliderstart)

while True:
    slider_values = camera.read_sliders()
    #gets values from sliders

    frame = camera.snap(camera0)
    camera.show_img(frame)
    mask = camera.show_mask(frame,slider_values)
    contours = camera.find_contours(mask)
    
    if(len(contours)>1):    #ckecks to make sure there are atleast two contours
        
        biggest_contour = max(contours, key=cv2.contourArea)
        remove_a(contours,biggest_contour)  #removes the biggest contour from contours
        second_biggest_contour = max(contours, key=cv2.c-ontourArea)
        
        camera.show_contour(biggest_contour,frame)
        camera.show_contour(second_biggest_contour,frame)
        c1 = camera.get_center(biggest_contour)
        c2 = camera.get_center(second_biggest_contour)
        c_obj = geo.mp(c1,c2)   #center of the obj
        v_obj = (c_obj,c1)  #defines a vector for the obj     
        ceta = geo.angle_of_vector(v_obj)   #finds the angle between the x axis and the vector
        print(ceta)
        
    if(camera.wait_for_exit(27,5)==1):   #key to exit, milliseconds to wait
        break
    
cv2.destroyAllWindows()
camera0.release()
