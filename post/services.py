from datetime import datetime


def check_tittle(title):
    """
    Function to check validate title
    :param title: str
    :return: presence of banned words
    """

    banned_words = ['ерунда', 'глупость', 'чепуха']
    count = 0
    for word in banned_words:
        if word in title:
            count += 1
        else:
            continue

    if count == 1:
        return True
    else:
        return False


def check_age(birthday):
    """
    Function to check validate birthday
    :param birthday: str(date-format)
    :return: less or more than 18 y.o.
    """
    date_now = datetime.now().date()
    if date_now.year - birthday.year <= 18:
        return True
    else:
        return False
