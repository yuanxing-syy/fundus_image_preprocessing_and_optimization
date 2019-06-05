# 眼底图像预处理及优化 
## 项目简介  
原始的眼底图 (参见path/in/image1.jpg）存在大量的黑边。这些背景像素对眼底图识别没有帮助。相反地，这些看似黑色的像素实际上存在噪声点，反而会起负面作用。因此，需要对眼底图做预处理，自动切出中间的圆形视野范围（circular field of view）该项目能够准确地切出眼底图圆形区域，并且经过优化后每张图像的处理速度从大约3s/张，降低到大约0.6s/张，切割精度不变，速度提升5倍左右
## 安装依赖
python 2.x  
OpenCV 3.1.0 (import cv2能成功就行)  
numpy 1.12.1  
## 实现原理 
<b>利用OpenCV和传统的图像处理方式去检测眼底图圆形边缘轮廓的点，根据这些点去拟合这个圆，求出圆心坐标和半径大小，最后在原图上直接截取即可</b>
## 实验效果 
代码执行  
```bash
$ python run.py
```
<img src="https://github.com/yuanxing-syy/fundus_image_preprocessing_and_optimization/raw/master/path/out/实验效果.png" width="60%" height="60%"></img>  
## 实验评价及优化 
优点：能精准切割圆形区域  

缺点：对图片的处理速度较慢，为2s多/张 

优化思路：

<img src="https://github.com/yuanxing-syy/fundus_image_preprocessing_and_optimization/raw/master/path/out/优化.png" width="60%" height="60%"></img>   
优化效果：相比于优化之前，精度略微下降，速度提高很多 

<img src="https://github.com/yuanxing-syy/fundus_image_preprocessing_and_optimization/raw/master/path/out/优化对比.png" width="60%" height="60%"></img> 