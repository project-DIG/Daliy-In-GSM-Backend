from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, on_delete = models.CASCADE, related_name='+')
    permission = models.ForeignKey('AuthPermission', on_delete = models.CASCADE, related_name='+')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete = models.CASCADE, related_name='+')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE, related_name='+')
    group = models.ForeignKey(AuthGroup, on_delete = models.CASCADE, related_name='+')

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE, related_name='+')
    permission = models.ForeignKey(AuthPermission, on_delete = models.CASCADE, related_name='+')

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    video = models.ForeignKey('Video', on_delete = models.CASCADE, related_name='+')
    commenter = models.ForeignKey('User', on_delete = models.CASCADE, related_name='+')
    content = models.TextField()
    like = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete = models.CASCADE, related_name='+', blank=True, null=True,)
    user = models.ForeignKey(AuthUser,on_delete = models.CASCADE, related_name='+')

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Follow(models.Model):
    user = models.ForeignKey('User',on_delete = models.CASCADE, related_name='+')
    target = models.ForeignKey('User',on_delete = models.CASCADE, related_name='+')

    class Meta:
        managed = False
        db_table = 'follow'


class Likes(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE, related_name='+')
    video = models.ForeignKey('Video', on_delete = models.CASCADE, related_name='+')
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'likes'


class Reply(models.Model):
    comment = models.ForeignKey('Comment', on_delete = models.CASCADE, related_name='+')
    commenter = models.ForeignKey('User', on_delete = models.CASCADE,related_name='+')
    content = models.IntegerField()
    like = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reply'


class User(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    profile_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Video(models.Model):
    title = models.CharField(max_length=45)
    video_url = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    tag = models.CharField(max_length=45)
    uploader = models.ForeignKey('User', on_delete = models.CASCADE, related_name='+')
    video_upload = models.FileField()

    class Meta:
        managed = False
        db_table = 'video'

