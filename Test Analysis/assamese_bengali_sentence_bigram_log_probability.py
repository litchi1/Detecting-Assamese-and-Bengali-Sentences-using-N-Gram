import json
import os.path

save_path = 'C:/Final Project Product/'

file_list = ['Assamese Files/assamese_train_corpus_bigram_log_probability.json',
             'Bengali Files/bengali_train_corpus_bigram_log_probability.json',
             'assamese_and_bengali_test_unordered_corpus.txt',
             'assamese_and_bengali_test_sentence_unordered_log_probability.json']

with open(os.path.join(save_path + file_list[0]), 'r', encoding='utf-8') as af:
    af_contents = json.load(af)


with open(os.path.join(save_path + file_list[1]), 'r', encoding='utf-8') as bf:
    bf_contents = json.load(bf)


data = dict()


def sent_break(my_list, j):
    sub_str = ' '.join(my_list[j: j + 2])
    return sub_str


with open(file_list[2], 'r', encoding='utf-8') as rf:
    for line in rf:
        as_adder = bn_adder = 0
        word = line.strip().split()
        length = len(word)

        for i in range(length):
            key = sent_break(word, i)
            if key in af_contents:
                as_adder += af_contents[key]
            else:
                as_adder += 0
            if key in bf_contents:
                bn_adder += bf_contents[key]
            else:
                bn_adder += 0

        if as_adder < bn_adder:
            data[line.strip()] = [as_adder, 'as']
        elif as_adder > bn_adder:
            data[line.strip()] = [bn_adder, 'bn']
        elif as_adder == bn_adder:
            data[line.strip()] = [2, 'unknown']  # any positive integer not decidable


with open(file_list[3], 'w', encoding='utf-8') as wf:
    json.dump(data, wf, ensure_ascii=False, indent=4)
