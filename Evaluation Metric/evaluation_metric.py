''' This program calculates the evaluation metrics for assamese sentences by analaysing
    assamese_and_bengali_test_unordered_corpus.txt to '''

import os.path
import json


save_path = 'C:/Final Project Product/'


file_list = ['Assamese Files/assamese_test_corpus.json',
             'Test Analysis/assamese_and_bengali_test_sentence_unordered_log_probability.json',
             'Evaluation Metric/assamese_and_bengali_test_sentence_evaluation_metric.txt']


tp = tn = fp = fn = 0


with open(os.path.join(save_path + file_list[0]), 'r', encoding='utf-8') as af:
    af_contents = json.load(af)

count = 0

with open(os.path.join(save_path + file_list[1]), 'r', encoding='utf-8') as rf:
    f_contents = json.load(rf)

    for line in f_contents:
        if line in af_contents:
            if af_contents[line] == f_contents[line][1]:
                tp += 1
            elif af_contents[line] != f_contents[line][1]:
                fn += 1
        else:
            if f_contents[line][1] == 'bn':
                tn += 1
            elif f_contents[line][1] == 'as':
                fp += 1


total = tp + tn + fp + fn

accuracy = (tp + tn) / total

precision = tp / (tp + fp)

recall = tp / (tp + fn)

f1score = 2 * ((precision * recall) / (precision + recall))


with open(os.path.join(save_path + file_list[2]), 'w', encoding='utf-8') as wf:
    wf.write(f'Total test sentences = {20000}\n\nEither Assamese or Bengali Sentences = {total}\n\n'
             f'Undetected sentences = {20000 - total}\n\n\n'
             f'Out of which::\n\n'
             f'True Positive = {tp}\n\nFalse Negative = {fn}\n\nTrue Negative = {tn}\n\nFalse Positive = {fp}\n\n\n\n'
             f'Accuracy = {accuracy}\n\nPrecision = {precision}\n\nRecall = {recall}\n\nF1-Score = {f1score}\n')
