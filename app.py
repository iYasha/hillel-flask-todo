from flask import Flask
from api.authorization import auth_api
from api.files import files_api
from pages.articles import article_pages
from pages.authorization import auth_pages
from api.articles import article_api

app = Flask(__name__)
app.register_blueprint(auth_api)
app.register_blueprint(article_api)
app.register_blueprint(files_api)
app.register_blueprint(auth_pages)
app.register_blueprint(article_pages)


if __name__ == '__main__':
	app.run(debug=True)
