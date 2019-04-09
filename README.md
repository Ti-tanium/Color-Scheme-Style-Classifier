# Style_classifier

# Image Crawler
The images used to train the classifier are crawled from <a href="https://www.freepik.com">FreePik<a/>. Three types of images are collected, including 'cute', 'fresh', 'technology'.
if you want to collect more types of images just add the type to the style list
 ``` 
  style=['cute','fresh','business'] 
 ```
  
 change the 'StartPage' and 'EndPage' variable to collect images from different pages
 
 ```
  StartPage=1
  EndPage=400
 ```
 The images are stored in the 'data' folder. And also, the color scheme (palette) is extracted using <a href="https://github.com/fengsp/color-thief-py">Color Theif</a>. Each palette is composed of 5 rgb colors.
 
 
 
 
