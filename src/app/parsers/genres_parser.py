from __future__ import annotations

import requests
from bs4 import BeautifulSoup
from config import TORRENT_IGRUHA_DOMEN
from loguru import logger

from app import db
from ..models import Genre


def update_genres_in_db() -> list[Genre]:
    try:
        r = requests.get(TORRENT_IGRUHA_DOMEN)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.content, features='lxml')

        div = soup.find('div', attrs={'class': 'content-right-column'})
        li_tags = div.find_all('li')

        genres = []
        for li in li_tags[5:]:
            href = li.a['href']
            if not href.startswith('https://'):
                genres.append(Genre(name=li.text, url=href))

        db.session.query(Genre).delete()
        db.session.add_all(genres)
        db.session.commit()

    except Exception as e:
        logger.error(e)
