from __future__ import print_function
import time
 


import cv2
import os
infilename ='./path/in/image1.jpg'
outfilename='./path/out/image1.jpg'

pathin="./path/in/"
pathout="./path/out/"
for i in os.listdir(pathin):
	in_img = cv2.imread(pathin+i)
	s_time = time.time()
	imc, dx, dy = em.mask(in_img)
	timecost = time.time() - s_time
	print ('mask time: %g seconds' % timecost)
	cv2.imwrite(pathout+i, imc, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
