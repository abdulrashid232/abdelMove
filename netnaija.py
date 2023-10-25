import requests
from bs4 import BeautifulSoup

def movie_link(movie_name):
    url = f'https://netnaija.xyz/{movie_name.replace(" ", "-")}'
    get_movie = requests.get(url).content
    soup = BeautifulSoup(get_movie, 'lxml')
    link_btn = soup.find('div', class_='wp-block-button')
    if link_btn:
        link = link_btn.a['href']
        return link
    return None
