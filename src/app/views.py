from app import (app, db)
from flask import (request, session, redirect,
                   url_for, render_template, flash)
from app.models import Genre

from app.parsers.genres_parser import update_genres_in_db
from app.parsers.gp_parser import get_game_desc, get_game_previews

from pprint import pprint


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html',
                           genres=db.session.query(Genre))


@app.route('/render_gp_content/')
@app.route('/render_gp_content/<string:url>/', methods=['post', 'get'])
@app.route('/render_gp_content/<genre>/<p>/<string:current_page>/',
           methods=['post', 'get'])
def render_gp_content(url='', genre='', current_page='', p=''):
    if not url:
        current_page = current_page or '1'
        url = f'{genre}/page/{current_page}/'

    game_previews, pages = get_game_previews(url)
    content_block = render_template(
        'gp_content_block.html',
        game_previews=game_previews,
        current_page=current_page
    )
    pagination_block = render_template(
        'pagination_block.html',
        pages=pages,
        current_page=current_page
    )
    return render_template('content_block.html',
                           content_block=content_block,
                           pagination_block=pagination_block)


@app.route('/get_game_preview_desc/<string:url>/')
def get_game_preview_desc(url: str):
    return get_game_desc(main_url=url)


@app.route('/render_genres_content/')
def render_genres_content():
    genres = db.session.query(Genre).all()
    content_block = render_template(
        'genres_content_block.html',
        genres=genres
    )
    return render_template('content_block.html',
                           content_block=content_block)


@app.route('/admin/')
def admin_panel():
    update_genres_in_db()
    return render_template('admin_panel.html')
