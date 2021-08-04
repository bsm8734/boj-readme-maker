#!/usr/bin/env python3
# coding: utf-8

import sys
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

__author__ = 'bsm8734'

'''
https://github.com/boostcamp-ai-tech-4/coding-test-study/sally/README.md
readme 작성을 빠르게 하기 위한 코드입니다.
'''

def get_problem_name(web_url):
    with urllib.request.urlopen(web_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title').get_text()
        print(title)
        return ' '.join(title.split(' ')[1:])


def make_urls(probs):
    base_url = 'https://www.acmicpc.net/problem/'
    names = []
    for p in probs:
        names.append(get_problem_name(base_url + p))
    return names


def make_readme(categ, probs, names):
    ''' Example

        ## Implementation

        - [ ] **3151_합이 0** / [문제](https://www.acmicpc.net/problem/3151) / [풀이]()
        - [ ] **20366_같이 눈사람 만들래?** / [문제](https://www.acmicpc.net/problem/20366) / [풀이]()
    '''

    base_url = 'https://www.acmicpc.net/problem/'
    file_path = './problem_list'

    f = open(file_path, 'w')
    f.write('## ' + categ + '\n\n') # title
    for prob, name in zip(probs, names):
        text = '- [ ] ' + prob + '_' + name + ' / [문제](' + base_url + prob + ') / [풀이]()  \n' # text
        f.write(text)
    f.close()


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
        main(sys.argv)
    # with Pycharm
    else:
        filename = 'Brute Force'
        prob_list = ['1969', '2503', '2422', '17626', '5568', '18511', '9079', '14501', '16937',
                     '16439', '2615', '16508', '14620', '12919', '1548', '2961', '15661', '1025',
                     '14500', '15686', '21278', '21315', '16637', '14391', '18808', ]
        main([''] + [filename] + prob_list)
