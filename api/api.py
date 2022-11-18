from flask import Blueprint, jsonify
from utils import get_posts_all
import logging
from logs.loggers import create_logger

create_logger()
logger = logging.getLogger('api')

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')


@api_blueprint.route('/posts/')
def api_all_posts():
    """
    :return: dict
    получает данные из JSON и возвращает список всех постов
    """
    logger.info('Запрос /api/posts')
    all_posts = get_posts_all()
    return jsonify(all_posts)


@api_blueprint.route('/posts/<int:post_id>')
def api_post_pk(post_id):
    """
    :param post_id: int
    :return:dict
    Получает номер поста в виде int:post_id и возвращает словарь с постом
    """
    logger.info(f"Запрос /api/posts/{post_id}")
    all_posts = get_posts_all()
    for post in all_posts:
        if post_id == post.get('pk'):
            return jsonify(post)
