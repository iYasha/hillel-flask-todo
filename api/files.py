import flask
from flask import request, send_file
from core import config, utils

files_api = flask.Blueprint('files_api', __name__)


@files_api.route(config.API_ROUTE_PREFIX + 'files/<filename>', methods=['GET'])
def get_file(filename):
	file_path = config.MEDIA_FOLDER + filename
	return send_file(file_path, attachment_filename=filename)
