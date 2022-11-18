import logging


def create_logger():
    """
    Эта функция создаст и настроит логгер basic
    """

    # Создаем логгер
    logger = logging.getLogger("api")
    logger.setLevel("INFO")

    # Добавляем обработчик – ошибки будут падать в консоль
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    # Добавляем обработчик – ошибки будут падать в файл
    file_handler = logging.FileHandler("./logs/api.log", encoding='UTF-8')
    logger.addHandler(file_handler)

    # Создаем форматтер и настраиваем вывод для обработчиков
    formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)


def logger_viewers():
    """
    Logger для main.views
    """

    logger = logging.getLogger("main")
    logger.setLevel("INFO")

    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("./logs/log.ini", encoding='UTF-8')
    logger.addHandler(file_handler)

    formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)


def set_logger_bookmarks():
    """
    Logger для bookmarks.views
    """

    logger = logging.getLogger("bookmarks")
    logger.setLevel("INFO")

    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("./logs/bookmarks.ini", encoding='UTF-8')
    logger.addHandler(file_handler)

    formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)
