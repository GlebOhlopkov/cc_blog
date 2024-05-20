from rest_framework import serializers

from users.services import check_domain, check_password


class EmailValidator:
    """
    Validator to check available of email
    """

    def __call__(self, value):
        email = value.get('email')
        if not check_domain(email):
            raise serializers.ValidationError(
                'You entered the wrong email. Allowed domains is mail.ru, yandex.ru')


class PasswordValidator:
    """
    Validator to check password
    """

    def __call__(self, value):
        password = value.get('password')
        if not check_password(password):
            raise serializers.ValidationError(
                'You entered simple password. Password must be at least 8 characters, must include any digits')
