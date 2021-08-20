import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image   # PIL是Python专业图像处理模块
from wordcloud import WordCloud

with open("alice.txt", "r+") as file:
    text = file.read()
    pass

wd = WordCloud(max_words=500, background_color="white").generate(text)

plt.figure()
plt.imshow(wd, interpolation="bilinear")
plt.axis("off")
plt.show()

alice_mask = np.array(Image.open("alice_mask.png"))
wd = WordCloud(max_words=500, background_color="white", mask=alice_mask).generate(text)

plt.figure()
plt.imshow(wd, interpolation="bilinear")
plt.axis("off")
plt.show()
