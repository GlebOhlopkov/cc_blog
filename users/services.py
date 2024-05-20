def check_domain(email):
    """
    Function to check validate email domain
    :param email: str
    :return: domain is validate
    """
    allowed_domains = ['mail.ru', 'yandex.ru']
    count = 0
    for domain in allowed_domains:
        if domain in email:
            count += 1
        else:
            continue

    if count == 1:
        return True
    else:
        return False


def check_password(password):
    """
    Function to check validate password
    :param password: str
    :return: password is validate
    """
    digits = '0123456789'
    if len(password) > 8 and any(char in digits for char in password):
        return True
    else:
        return False
