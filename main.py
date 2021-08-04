#!/usr/bin/env python3
# coding: utf-8

import sys
from utils import make_urls, make_readme, find_problems

__author__ = 'bsm8734'

'''
https://github.com/boostcamp-ai-tech-4/coding-test-study/sally/README.md
readme 작성을 빠르게 하기 위한 코드입니다.
'''


def main(args):
    category_name, probs = args[1], args[2:]

    print('category: ', category_name)
    print('problems', probs)

    names = make_urls(probs)
    make_readme(category_name, probs, names)

    print('done')


if __name__ == '__main__':
    # with Terminal
    if len(sys.argv) > 1:
        print('Runing... custom arguments...')
        main(sys.argv)
    # with Pycharm
    else:
        print('Runing... default parameters...')
        filename = 'Brute Force'
        prob_list = ['1969', '2503', '2422', '17626', '5568', '18511', '9079', '14501', '16937',
                     '16439', '2615', '16508', '14620', '12919', '1548', '2961', '15661', '1025',
                     '14500', '15686', '21278', '21315', '16637', '14391', '18808', ]
        main([''] + [filename] + prob_list)
