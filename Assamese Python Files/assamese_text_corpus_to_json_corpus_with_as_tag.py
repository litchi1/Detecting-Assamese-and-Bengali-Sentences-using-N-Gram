''' This program converts the assamese_text_corpus.txt to assamese_text_corpus.json for finding of evaluation metric.'''

import json
import os.path


save_path = 'C:/Final Project Product/Assamese Files/'

file_list = ['assamese_unique_test_corpus.txt', 'assamese_test_corpus.json']

data = dict()


with open(os.path.join(save_path + file_list[0]), 'r', encoding='utf-8') as rf:
    for line in rf:

        data[line.strip()] = 'as'


with open(os.path.join(save_path + file_list[1]), 'w', encoding='utf-8') as wf:
    json.dump(data, wf, ensure_ascii=False, indent=4)


