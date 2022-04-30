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
		return utils.error(4, 'Некорректный email')
	if len(list(filter(lambda x: x['email'] == email, users))) != 0:
		return utils.error(2, 'Пользователь с таким email уже зарегистрирован')
	if password is None or len(password) < 6:
		return utils.error(5, 'Пароль должен быть не менее 6 символов')
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
	return utils.error(6, 'Неверный email или пароль')


@auth_api.route(config.API_ROUTE_PREFIX + 'user/me', methods=['GET'])
def get_user_info():
	global users
	"""
	Authorization: Bearer hV7g1pxCmWnJb3cY5KDY
	"""
	authorization_header = request.headers.get('Authorization')
	if authorization_header is None:
		return utils.error(7, 'Не передан заголовок Authorization')
	access_token = authorization_header.split()[1]
	for user in users:
		if user['access_token'] == access_token:
			return flask.jsonify({
				'code': 0,
				'message': 'User found',
				'user': user
			})
	return utils.error(8, 'Некорректный токен авторизации')
