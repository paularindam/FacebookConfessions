from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import warnings
import pygame

#sys.path.append("/Users/arindam/Downloads/Imaging-1.1.7")
#from PIL import *
from PIL import Image, ImageDraw, ImageFont
warnings.filterwarnings("ignore", category=DeprecationWarning) 

with open("constitution.txt") as f:
    lines = f.readlines()                                                                            
    text = "".join(lines)  

cv = CountVectorizer(min_df=0, charset_error="ignore",stop_words="english", max_features=200)
counts = cv.fit_transform([text]).toarray().ravel() 
words = np.array(cv.get_feature_names()) 
counts = counts / float(counts.max())

img_grey = Image.new("L", (200, 200))
draw = ImageDraw.Draw(img_grey)
#font_path= pygame.font.get_default_font()
font_path = "/Library/Fonts/Tahoma.ttf"
font_size = 24
font = ImageFont.truetype(font_path, font_size)
draw.setfont(font)
draw.text((50, 40), "Text that will appear in white", fill="white")

#area = (integral_image[w:, h:] + integral_image[:w, :h]
 #       - integral_image[w:, :h] - integral_image[:w, h:])





