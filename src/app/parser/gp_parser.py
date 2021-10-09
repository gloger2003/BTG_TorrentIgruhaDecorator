"""
Парсер превью игр и ссылок на них
"""

from __future__ import annotations

import requests
from bs4 import BeautifulSoup
from config import TORRENT_IGRUHA_DOMEN
from loguru import logger

from app.datatypes import GamePreview


def get_game_previews(main_url: str):
    pages = []
    game_previews: list[GamePreview] = []

    if not main_url.startswith('https'):
        main_url = TORRENT_IGRUHA_DOMEN + main_url[0:]

    try:
        r = requests.get(main_url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.content, features='lxml')

        divs = soup.find_all(class_='article-film')

        # Карточки
        for div in divs:
            title = div.find('div', attrs={'class': 'article-film-title'}).text
            image = div.find(
                'div', attrs={'class': 'article-film-image'}).a.img['src']
            url = div.find(
                'div', attrs={'class': 'article-film-image'}).a['href']

            url = url.replace(TORRENT_IGRUHA_DOMEN, '')
            game_previews.append(GamePreview(title, image, url))

        # Страницы
        try:
            page_div = soup.find('div', id='pages')
            for tag in page_div.childGenerator():
                if not tag.text == ' ':
                    url: str = ''
                    try:
                        url = tag['href']
                        url = url.replace(TORRENT_IGRUHA_DOMEN, '')
                    except Exception as e:
                        pass

                    text = tag.text.strip()

                    # Нужно сократить
                    if text == '...':
                        url = ''
                    else:
                        if not url:
                            url = 'current'

                    pages.append((text, url))
        except Exception as e:
            logger.error(e)
    except Exception as e:
        logger.error(e)

    return game_previews, pages


def get_game_desc(main_url: str):
    if not main_url.startswith('https'):
        main_url = TORRENT_IGRUHA_DOMEN + main_url[0:]

    r = requests.get(main_url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, features='lxml')

    desc_div = soup.find('div', class_="blockinfo")
    desc_str = desc_div.text[0:401] + '...'
    return desc_str
