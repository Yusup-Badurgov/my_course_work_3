class View:
    """
    Обрабатывает экземпляр класса с просмотренными постами
    Добавляет pk поста во множество и проверяет на просмотр ранее
    """

    def __init__(self):
        self.view_posts = set()
        self.like_posts = set()

    def get_add_view(self, pk):
        self.view_posts.add(pk)

    def get_views(self):
        return self.view_posts

    def get_verify_view(self, pk):
        if pk in self.view_posts:
            return True
        else:
            return False

    def get_like_add(self, pk):
        self.like_posts.add(pk)

    def get_like_discard(self, pk):
        self.like_posts.discard(pk)

    def get_like(self):
        return self.like_posts

    def get_verify_like(self, pk):
        if pk in self.like_posts:
            return True
        else:
            return False
