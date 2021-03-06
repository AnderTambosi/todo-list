import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, \
    PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .', 'invalid'
            )
        ],
        help_text='Um nome curto que será usado para'
                  'identificá-lo de forma única na plataforma'
    )
    name = models.CharField(
        u'Nome',
        max_length=100,
        blank=True
    )
    email = models.EmailField(
        'E-mail',
        unique=True
    )
    cpf = models.CharField(
        u'CPF',
        max_length=20
    )
    GENDERS = (
        ('male', 'Masculino'),
        ('female', 'Feminino')
    )
    gender = models.CharField(
        u'Gênero',
        max_length=20,
        null=True,
        blank=True,
        choices=GENDERS
    )
    is_staff = models.BooleanField(
        u'Equipe',
        default=False
    )
    is_active = models.BooleanField(
        'Ativo',
        default=True
    )
    date_joined = models.DateTimeField(
        'Data de Entrada',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
