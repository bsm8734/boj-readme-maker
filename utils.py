from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

FILEPATH = './problem_list'

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
    file_path = FILEPATH

    f = open(file_path, 'w')
    f.write('## ' + categ + '\n\n') # title
    for prob, name in zip(probs, names):
        text = '- [ ] ' + prob + '_' + name + ' / [문제](' + base_url + prob + ') / [풀이]()  \n' # text
        f.write(text)
    f.close()


def find_problems(categ_name, url):
    probs = []
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for details in soup.find('div', {'id': 'readme'}).find_all('details'):
            title = details.find('summary').find('strong').get_text()
            if categ_name in title:
                for tr in details.find('tbody').find_all('tr'):
                    probs.append(tr.find('a').get_text())
    return probs