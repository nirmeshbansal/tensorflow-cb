import tensorflow as tf
import pandas as pd
import numpy
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(num_words = 5, oov_token = '-1')
trainset = pd.read_csv('aossie-click-bait-dataset/clickBait_Data.csv')
print(df.head())
del trainset['index']
del trainset['id']
del trainset['clickbait']
trainlabel = pd.read_csv('aossie-click-bait-dataset/clickBait_Data.csv')
del trainlabel['index']
del trainlabel['id']
del trainlabel['titles']
tokenizer = Tokenizer()
tokenizer.fit_on_texts(trainset)
