''' This program takes the assamese_train_corpus.txt and slides one word each sentence to create
    one word and caluclate each frequencies. Similarly it slides two words each sentence to create
    two word and calculate each frequencies. '''


import os.path
import json
from collections import Counter

word_list = list()

save_path = 'C:/Final Project Product/Assamese Files/'

file_list = ['assamese_train_corpus_one_word.txt', 'assamese_train_corpus_two_word.txt',
             'assamese_train_corpus_one_word_count.json', 'assamese_train_corpus_two_word_count.json']


with open(os.path.join(save_path + file_list[1]), 'r', encoding='utf-8') as rf:
    for line in rf:
        word_list.append(line.strip())


count = dict(Counter(word_list))

json = json.dumps(count, ensure_ascii=False, indent=4)

with open(os.path.join(save_path + file_list[3]), 'w', encoding='utf-8') as wf:
    wf.write(json)

