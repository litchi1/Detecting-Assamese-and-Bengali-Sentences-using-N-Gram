''' This program takes two files assamese_test.txt and bengali_test.txt, appends it to a single file assamese_and_
    bengali_test_unordered_corpus.txt in which an assamese sentence is followed by a bengali sentence and vice-versa.'''

import os.path


save_path = 'C:/Final Project Product/'

file_list = ['Assamese Files/assamese_unique_test_corpus.txt', 'Bengali Files/bengali_unique_test_corpus.txt',
             'Test Analysis/assamese_and_bengali_test_unordered_corpus.txt']


with open(os.path.join(save_path + file_list[0]), 'r', encoding='utf-8') as rf1:
    with open(os.path.join(save_path + file_list[1]), 'r', encoding='utf-8') as rf2:
        with open(os.path.join(save_path + file_list[2]), 'w', encoding='utf-8') as wf:
            for line1, line2 in zip(rf1, rf2):
                wf.write(f'{line1.strip()}\n{line2.strip()}\n')
