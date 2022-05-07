import flask
from flask import request
from datetime import datetime

from core import config
from crud.articles import article_crud

article_api = flask.Blueprint('article_api', __name__)

"""
0) ID
1) Title (Заголовок)
2) Content (Содержимое)
3) Author (Автор)
4) Created Date (Дата создания)

/articles - GET (Получение всех статей)
/articles - POST (Создание новой статьи)
/articles/<int:id> - GET (Получение статьи по идентификатору)

ДЗ:
/articles/<int:id> - PUT (Обновление статьи по идентификатору)
/articles/<int:id> - DELETE (Удаление статьи по идентификатору)
"""


@article_api.get(config.API_ROUTE_PREFIX + 'articles')
def get_articles():
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.get_all()
		})


@article_api.get(config.API_ROUTE_PREFIX + 'articles/<id>')
def get_article(id):
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.get_one(id)
		})


@article_api.post(config.API_ROUTE_PREFIX + 'articles')
def create_article():
	if 'title' not in request.json or 'content' not in request.json or 'author' not in request.json:
		return flask.jsonify({
				'code': 9,
				'message': 'Title, content, author являются обязательными полями',
				'data': None
			})
	request.json['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.create(request.json)
		})

