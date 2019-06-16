''' This program divides the two word frequencies by one word frequencies if the first word of two words matches
    with one word to create the bigram count and take its log value.'''

import os.path
import json
from math import log

save_path = 'C:/Final Project Product/Assamese Files/'

file_list = ['assamese_train_corpus_one_word_count.json', 'assamese_train_corpus_two_word_count.json',
             'assamese_train_corpus_bigram_log_probability.json']


with open(os.path.join(save_path + file_list[0]), 'r', encoding='utf-8') as of:
    of_contents = json.load(of)


with open(os.path.join(save_path + file_list[1]), 'r', encoding='utf-8') as tf:
    tf_contents = json.load(tf)


data = dict()


for tf_key, tf_value in tf_contents.items():
    key = tf_key.split()
    if key[0] in of_contents:
        result = log(tf_value / of_contents[key[0]])
        data[tf_key] = result

with open(os.path.join(save_path + file_list[2]), 'w', encoding='utf-8') as wf:
    json.dump(data, wf, ensure_ascii=False, indent=4)
