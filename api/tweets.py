import string
import random

import flask
from flask import request
from datetime import datetime

from pydantic import ValidationError

from core import config

from crud.articles import article_crud
from schemas.articles import Article


"""
Задание:
Написать API для создания/редактирования/удаления/получения твитов используя модели PyDantic

Твит содержит следующие поля:
0) ID - генерируется автоматически
1) Текст твита
2) Автор твита
3) Дата создания твита - генерируется автоматически
"""

from schemas.tweets import Tweet
from crud.tweets import tweet_crud


tweets_api = flask.Blueprint('tweets_api', __name__)


@tweets_api.get(config.API_ROUTE_PREFIX + 'tweet')
def get_all_tweets():
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': tweet_crud.get_all()
		})


@tweets_api.get(config.API_ROUTE_PREFIX + 'tweet/<id>')
def get_one_tweet(id):
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': tweet_crud.get_one(id)
		})


@tweets_api.post(config.API_ROUTE_PREFIX + 'tweet')
def create_tweet():
	try:
		tweet = Tweet(
			text=request.json.get('text'), author=request.json.get('author'),
		)
	except ValidationError as e:  # Отловили ошибку PyDantic и записали ее в переменную e
		return e.json()  # Преобразовали ошибку в JSON и вернули ее
	return flask.jsonify(
		{
			'code': 0,
			'message': 'OK',
			'data': tweet_crud.create(tweet.dict())
		}
	)


@tweets_api.put(config.API_ROUTE_PREFIX + 'tweet/<id>') 
def put(id):
	try:
		tweet = Tweet(
			id=str(id), title=request.json.get('text'), content=request.json.get('author')
		)
	except ValidationError as e:  # Отловили ошибку PyDantic и записали ее в переменную e
		return e.json()  # Преобразовали ошибку в JSON и вернули ее
	data = tweet_crud.update(tweet.dict(), id)
	if data is None:
		return flask.jsonify(
			{
				'code': 9,
				'message': 'Статья не найдена',
				'data': None
			}
		)
	return flask.jsonify(
		{
			'code': 0,
			'message': 'OK',
			'data': None
		}
	)


@tweets_api.delete(config.API_ROUTE_PREFIX + 'tweet/<id>')
def delete_article(id):
	return flask.jsonify(
		{
			'code': 0,
			'message': 'delete article',
			'data': tweet_crud.delete(id)
		}
	)