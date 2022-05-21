import flask

article_pages = flask.Blueprint('article_pages', __name__)


@article_pages.route('/articles', methods=['GET'])
def get_all_articles():
	return flask.render_template('articles.html')
