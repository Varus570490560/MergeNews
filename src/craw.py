import os

import requests
from bs4 import BeautifulSoup


def find_a(soup):
    return soup.findAll(name='a')


def visit_page(urls):
    base_url = 'https://www.ign.com'
    for url in urls:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
        }
        response = requests.get(url='https://www.ign.com'+url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        title = soup.find(name='title')
        path = './output/' + title.string
        if not os.path.isdir(path):
            os.makedirs(path)
        with open('./output/' + title.string + '/' + title.string + '.txt', 'wb') as writer:
            ps = soup.findAll(name='p')
            update = soup.find(name='div', attrs='jsx-2034901901 article-modified-date')
            if update is not None:
                writer.write(update.text.encode())
                writer.write('\n'.encode())
            for p in ps:
                print(p)
                writer.write(p.text.encode())
                writer.write('\n'.encode())
                writer.flush()


def run_browser():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    response = requests.get(url='https://www.ign.com', headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    urls = find_a(soup=soup)
    res = list()
    for url in urls:
        if url['href'].startswith('/news/') or url['href'].startswith('/wikis/') or url['href'].startswith(
                '/videos/') or url['href'].startswith('/articles/'):
            res.append(url['href'])
    return res
