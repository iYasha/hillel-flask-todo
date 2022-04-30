import flask
from flask import request
from core import config, utils

users = []
auth_api = flask.Blueprint('auth_api', __name__)


@auth_api.route(config.API_ROUTE_PREFIX + 'register', methods=['POST'])
def register():
	global users
	data = request.json
	full_name = data.get('full_name')
	email = data.get('email')
	password = data.get('password')
	if email is None or email.find('@') == -1 or email.find('.') == -1:
		return flask.jsonify(
			{
				'code': 4,
				'message': 'Incorrect email'
			}
		)
	if len(list(filter(lambda x: x['email'] == email, users))) != 0:
		return flask.jsonify(
			{
				'code': 2,
				'message': 'Пользователь уже есть в системе'
			}
		)
	if password is None or len(password) < 6:
		return flask.jsonify(
			{
				'code': 5,
				'message': 'Incorrect password'
			}
		)
	user = {
		'full_name': full_name,
		'email': email,
		'password': utils.hash_password(password),
		'access_token': utils.generate_access_token()
	}
	users.append(user)
	return flask.jsonify({
			'code': 0,
			'message': 'User registered!',
			'user': user
		})


@auth_api.route(config.API_ROUTE_PREFIX + 'login', methods=['POST'])
def login():
	global users
	data = request.json
	email = data.get('email')
	password = data.get('password')

	for user in users:
		if user['email'] == email and utils.check_password(user['password'], password):
			access_token = utils.generate_access_token()
			user['access_token'] = access_token
			return flask.jsonify({
					'code': 0,
					'message': 'User logged in!',
					'access_token': access_token
				})
	return flask.jsonify({
			'code': 6,
			'message': 'Такого пользователя нет в системе'
		})


@auth_api.route(config.API_ROUTE_PREFIX + 'user/me', methods=['GET'])
def get_user_info():
	global users
	"""
	Authorization: Bearer hV7g1pxCmWnJb3cY5KDY
	"""
	access_token = request.headers.get('Authorization').split()[1]
	for user in users:
		if user['access_token'] == access_token:
			return flask.jsonify({
				'code': 0,
				'message': 'User found',
				'user': user
			})
	return flask.jsonify({
		'code': 7,
		'message': 'У вас нет секретного ключа'
	})