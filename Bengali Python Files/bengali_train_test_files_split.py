'''This program splits the entire bengali_corpus.txt into 80% bengali_train_corpus.txt and
    20% bengali_test_corpus.txt'''

import os.path

file_list = ['bengali_corpus.txt', 'bengali_train_corpus.txt', 'bengali_test_corpus.txt']

save_path = 'C:/Final Project Product/Bengali Files/'

count = 0

with open(os.path.join(save_path + file_list[0]), 'r', encoding='utf-8') as rf:
    with open(os.path.join(save_path + file_list[1]), 'w', encoding='utf-8') as wf1:
        with open(os.path.join(save_path + file_list[2]), 'w', encoding='utf-8') as wf2:
            for line in rf:
                count += 1
                if count < 40001:
                    wf1.write(f'{line.strip()}\n')
                elif 40001 <= count < 50001:
                    wf2.write(f'{line.strip()}\n')
