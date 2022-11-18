from flask import Flask, send_from_directory
from main.views import main_blueprint
from bookmarks.views import bookmarks_blueprint
from api.api import api_blueprint

POST_PATH = 'data/posts.json'
UPLOAD_FOLDER = 'uploads/images'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
# обработка запросов
app.register_blueprint(bookmarks_blueprint)
# избранные посты
app.register_blueprint(api_blueprint)
# создан по заданию для тестирования API


@app.errorhandler(404)
def page_404(error):
    return "404 NOT FOUND"


@app.errorhandler(500)
def page_500(error):
    return "500 Internal Server Error"


@app.route('/uploades/<path:path>')
def static_dir(path):
    return send_from_directory('uploades', path)


if __name__ == '__main__':
    app.run()