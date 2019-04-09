# Style_classifier
This repository trained a classifier to differentiate different style of color scheme, such as cute, fresh or technology.
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
 The images are stored in the 'data' folder. And also, the color scheme (palette) is extracted using <a href="https://github.com/fengsp/color-thief-py">Color Theif</a>. Each palette is composed of 5 rgb colors, and stored in 'train_2.csv', which looks like this:
 
 <img src="images/traincsv.jpg"/>
 
 Below is a example of color scheme extraction.
 
 Image:
 
 <img src="./data/cute/cute_4.jpg" style="width:100px;height=100px" />
 
 Extracted color scheme:
 
 <img src="./images/cute_4.jpg">
 
 # Classfier
 The classifer is trained using lightGBM. The data set has 30 features(5*3 rgb and 5*3 hls). The multi_error of the model is arround 32% (it's a little bit high:eyes:), there is still a long way to go. Any suggestion would be appreciated:blush:.
 The detailed code is in the 'classifyPalette.ipynb' notebook. If you are not interested in the detailed training process, you can also use 'stylePredict.py' to do color scheme pridiction.
 
 ## Usage
 ### Prerequisite
 make sure you have the following module installed:
 ```
 pip install lightgbm
 pip install colorthief
 pip install pandas
 ```
  Download model.txt and stylePredict.py and you can use the style_predict function to predict color scheme style. The parameter is a list of 5 rgb tuples(eg：[(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b)]). And it returns three styles ['cute','fresh','technology'].
  
  Hear is two examples:
  
  Image:
  
  <img src="./data/cute/cute_600.jpg" />

  Palette: [(240, 224, 225),(144, 198, 216),(241, 40, 114),(221, 185, 54),(47, 177, 205)]
  
  Predictions:
  
  <img src="./images/cute_600.jpg">
  
  
  Image:
  
  <img src="./data/technology/technology_600.jpg" />

  Palette: [(46, 175, 231), (76, 140, 144), (9, 102, 179), (6, 71, 130), (4, 23, 47)]
  
  Predictions:
  
  <img src="./images/technology_600.jpg">
  
  
  Because the color schemes extracted from images of different style may only differentiate slightly from each other, it's difficult for the classifier to distinguish these palettes. Given a better dataset, the results may improve a lot.

 
