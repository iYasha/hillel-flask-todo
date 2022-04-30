import flask

auth_pages = flask.Blueprint('auth_pages', __name__)


@auth_pages.route('/register', methods=['GET'])
def get_register_page():
	return flask.render_template('register.html')


@auth_pages.route('/me', methods=['GET'])
def get_login_page():
	return flask.render_template('me.html')
