#!/usr/bin/env python3
# coding: utf-8

import sys
from utils import make_urls, make_readme, find_problems

__author__ = 'bsm8734'

'''
src_format: https://github.com/boostcamp-ai-tech-4/coding-test-study/README.md
dst_format: https://github.com/boostcamp-ai-tech-4/coding-test-study/sally/README.md
readme 형식을 빠르게 변형하기 위한 코드입니다.
'''

def main(category_name, url):
    probs = find_problems(category_name, url)

    print('category: ', category_name)
    print('problems', probs)

    names = make_urls(probs)
    make_readme(category_name, probs, names)

    print('done')


if __name__ == '__main__':
    url = 'https://github.com/boostcamp-ai-tech-4/coding-test-study/blob/main/README.md'

    # with Terminal
    if len(sys.argv) > 1:
        print('Runing... custom arguments...')
        main(sys.argv[1], url)
    # with Pycharm
    else:
        print('Runing... default parameters...')
        category_name = '투 포인터'
        main(category_name, url)

