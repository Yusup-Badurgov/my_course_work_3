from flask import Blueprint, render_template, request
from utils import get_posts_all, get_posts_bookmarks, get_comments_by_post_id, get_post_by_pk, get_posts_by_user, \
    search_for_posts, get_tag, get_like
import logging
from logs.loggers import logger_viewers

logger_viewers()
logger_main = logging.getLogger('main')

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')


@main_blueprint.route('/')
def page_index():
    posts = get_posts_all()
    count_bookmarks = len(get_posts_bookmarks())
    logger_main.info(f'Запрос главной страницы')
    return render_template('index.html', posts=posts, count_bookmarks=count_bookmarks)


@main_blueprint.route('/posts/<int:post_id>')
def page_post(post_id):
    comments = get_comments_by_post_id(post_id)
    post = get_post_by_pk(post_id)
    count_comment = len(comments)
    logger_main.info(f'Запрос /posts/{post_id}')
    return render_template('post.html', post=post, comments=comments, count=count_comment)


@main_blueprint.route('/posts/<user_name>')
def page_posts_user(user_name):
    all_post_user = get_posts_by_user(user_name)
    logger_main.info(f'Запрос /posts/{user_name}')
    return render_template('user-feed.html', posts=all_post_user)


@main_blueprint.route('/search')
def page_search():
    query = request.args.get('q')
    if query and query != '':
        posts = search_for_posts(query)
        count_posts = len(posts)
        logger_main.info(f'Запрос /search/{query}')
    return render_template('search.html', posts=posts, count_posts=count_posts, tag=query)


@main_blueprint.route('/tag/<tagname>')
def page_tag(tagname):
    posts = get_tag(tagname)
    logger_main.info(f'Запрос /tag/{tagname}')
    return render_template('tag.html', posts=posts, tag=tagname)

@main_blueprint.route('/like/<int:postid>')
def push_like(postid):

    like = get_like(postid)

    comments = get_comments_by_post_id(postid)
    post = get_post_by_pk(postid)
    count_comment = len(comments)
    logger_main.info(f'Запрос /posts/{postid}')
    print(like)
    return render_template('post.html', post=post, comments=comments, count=count_comment)

