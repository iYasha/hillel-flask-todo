import random
import string
import hashlib
import json

from core import config


def generate_access_token() -> str:
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(config.ACCESS_TOKEN_LEN))


def hash_password(password):
	encoded_password = (password + config.SALT).encode('utf-8')
	return hashlib.sha256(encoded_password).hexdigest()


def check_password(hashed_password, user_password):
	return hashed_password == hash_password(user_password)


def error(code: int, message: str) -> str:
	return json.dumps({
			'code': code,
			'message': message
		})

