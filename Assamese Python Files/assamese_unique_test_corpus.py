''' This program writes only unique assamese test sentences to form a corpus for test analysis.'''

from collections import Counter
import os.path

save_path = 'C:/Final Project Product/Assamese Files/'

file_list = ['assamese_test_corpus.txt', 'assamese_unique_test_corpus.txt']

my_list = list()

with open(os.path.join(save_path + file_list[0]), 'r', encoding='utf-8') as rf:
    for line in rf:
        my_list.append(line.strip())

    count = dict(Counter(my_list))


with open(os.path.join(save_path + file_list[1]), 'w', encoding='utf-8') as wf:
    for key, value in count.items():
        wf.write(f'{key.strip()}\n')
