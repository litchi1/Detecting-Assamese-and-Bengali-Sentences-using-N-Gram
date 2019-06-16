''' This program splits the assamese_train_corpus.txt into uni-gram, bi-gram,
    tri-gram, etc. according to user requirements. '''

import os.path

save_path = 'C:/Final Project Product/Assamese Files/'

file_list = ['assamese_train_corpus_one_word.txt', 'assamese_train_corpus_two_word.txt',
             'assamese_train_corpus_three_word.txt']

ngram = int(input('Enter the value of ngram:: '))

with open(os.path.join(save_path + 'assamese_train_corpus.txt'), 'r', encoding='utf-8') as rf:
    with open(os.path.join(save_path + file_list[ngram - 1]), 'w', encoding='utf-8') as wf:
        for line in rf:
            word = line.strip().split()
            length = len(word) - 1

            for i in range(length):
                sub_str = ' '.join(word[i: i + ngram])
                wf.write(f'{sub_str.strip()}\n')
