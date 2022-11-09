from django.db import models

class User(models.Model):
    nickname = models.CharField('NICKNAME', max_length=20)
    profile_image = models.URLField('PROFILE_IMAGE', max_length=255)
    email = models.EmailField('EMAIL', max_length=255, unique=True)
    bio = models.TextField('BIO')