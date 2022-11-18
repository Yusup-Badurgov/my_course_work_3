import json
import os
from json import JSONDecodeError

from post_view import View

views = View()


def read_json(file_name):
    """
    :param file_name: str
    :return: list
    получает имя JSON файла, считывает файл
    и возвращает список словарей
    """
    try:
        with open(file_name, 'r', encoding='UTF-8') as read_file:
            return json.load(read_file)
    except FileNotFoundError:
        return
    except JSONDecodeError:
        return


def save_json(file_name, data_for_save):
    """
    :param file_name: str
    :param data_for_save: str
    Получает данные data_for_save и имя файла save_file
    для сохранения JSON
    """
    try:
        with open(file_name, 'w', encoding='UTF-8') as save_file:
            json.dump(data_for_save, save_file, ensure_ascii=False)
    except FileNotFoundError:
        return
    except JSONDecodeError:
        return


def get_posts_all():
    return read_json('data/posts.json')


def get_posts_by_user(user_name):
    """
    :param user_name: str
    :return: list
    Формирует список словарей по ключу poster_name
    """
    error = True
    all_posts = read_json('data/posts.json')
    all_post_user = []
    for post in all_posts:
        if user_name.lower() == post.get('poster_name').lower():
            all_post_user.append(post)
            error = False
    if error:
        raise ValueError(f'пользователь {user_name} не найден')
    return all_post_user


def get_comments_by_post_id(post_id):
    """
    :param post_id:int
    :return: list
    Формирует список словарей с комментами к посту по ключу post_id
    """
    all_comments = read_json('data/comments.json')

    all_posts = read_json('data/posts.json')
    # читает все посты, чтобы проверить существование поста для исключения ValueError
    error = True
    for post in all_posts:
        if post_id == post.get('pk'):
            error = False
            break
    if error:
        raise ValueError(f'пост {post_id} отсутствует')
    else:
        return [comment for comment in all_comments if post_id == comment.get('post_id')]


def search_for_posts(query):
    """
    :param query: str
    :return: list
    Формирует список словарей с постами, содержащими запрошенное значение query
    """
    all_posts = read_json('data/posts.json')
    return [post for index, post in enumerate(all_posts) if query.lower() in post.get("content").lower() and index < 10]


def get_post_by_pk(pk):
    """
    :param pk: int
    :return: dict
    Возвращает словарь выбранного поста по его 'pk'.
    класс View добавлен с целью проверки на просмотры,
    чтобы избежать накручивание счетчика при каждом клике на пост
    """
    all_posts = read_json('data/posts.json')
    views_verify = views.get_verify_view(pk)
    for index, post in enumerate(all_posts):
        if pk == post.get('pk') and views_verify:
            return post
        elif pk == post.get('pk') and views_verify is False:
            views.get_add_view(pk)
            all_posts[index]['views_count'] += 1
            save_json('data/posts.json', all_posts)
            return post

def get_like(postid):
    all_posts = read_json('data/posts.json')
    verify_like = views.get_verify_like(postid)
    for index, post in enumerate(all_posts):
        if postid == post.get('pk') and verify_like:
            views.get_like_discard(postid)
            all_posts[index]['likes_count'] -= 1
            save_json('data/posts.json', all_posts)
            return post

        elif postid == post.get('pk') and verify_like is False:
            views.get_like_add(postid)
            all_posts[index]['likes_count'] += 1
            save_json('data/posts.json', all_posts)
            return post



def add_bookmarks(postid):
    """
    :param postid:
    :return: list

    Функция реализует проверку перед добавлением поста в список bookmarks,
    добавляет значение 'pk', в случае отсутствия
    и возвращает список bookmarks.
    Т.к.JSON содержит только 'pk', это позволяет избежать дополнительной итерации
    при проверке, а так же всегда загружает обновленные посты, в отличии, если
    в bookmarks хранились бы посты полностью.
    """
    posts_in_bookmarks = read_json('data/bookmarks.json')
    if postid not in posts_in_bookmarks:
        posts_in_bookmarks.append(postid)
        save_json('data/bookmarks.json', posts_in_bookmarks)
    return posts_in_bookmarks


def remove_bookmarks(postid):
    """
    :param postid: int
    :return: list
    Удаляет пост по параметру postid
    Пересохраняет обновленный список словарей и возвращает его
    """
    posts_in_bookmarks = read_json('data/bookmarks.json')
    # добавлено для проверки на наличие поста в списке bookmarks перед удалением
    if postid in posts_in_bookmarks:
        posts_in_bookmarks.remove(postid)
        save_json('data/bookmarks.json', posts_in_bookmarks)
    return posts_in_bookmarks


def get_posts_bookmarks():
    """
    :return: list
     Возвращает список словарей для вывода в bookmarks
    """
    posts_in_bookmarks = read_json('data/bookmarks.json')
    all_posts = get_posts_all()
    return [post for post in all_posts if post.get('pk') in posts_in_bookmarks]


def get_tag(tagname):
    """
    :param tagname: str
    :return: list
    Формирует список словарей ао запрошенному параметру tagname
    """
    all_posts = read_json('data/posts.json')
    return [post for post in all_posts if f'#{tagname}' in post.get('content')]
