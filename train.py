import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(num_words = 5, oov_token = '-1')
sentence = ['hello boi you are weird','sup my niggsy piggsy as as as as fd fdf e ed sc gdf s e s as das fdaf ']
tokenizer.fit_on_texts(sentence)
word_index = tokenizer.word_index
print(word_index)