import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud

df = pd.read_csv('output1.csv')
hashtags = []

for info_list in df["hashtagInfo"]:
    if isinstance(info_list, str):  # Check if the value is a string
        info_list = eval(info_list)  # Convert the string representation of list to list
        for info_dict in info_list:
            if "hashtagName" in info_dict:
                hashtags.append(info_dict["hashtagName"])

#Creation of wordcloud
wordcloud = WordCloud(
    max_font_size=100,
    max_words=100,
    background_color="black",
    scale=10,
    width=800,
    height=800
).generate(' '.join(hashtags))
#Figure properties
plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()