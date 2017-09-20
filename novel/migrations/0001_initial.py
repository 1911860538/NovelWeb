# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 10:52
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=32)),
                ('avatar', models.ImageField(default='', upload_to='user/%Y/%m', verbose_name='头像')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=255, verbose_name='文章描述')),
                ('avatar', models.ImageField(default='', upload_to='article/%Y/%m', verbose_name='头像')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Article2Tag',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.Article', verbose_name='文章')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('nid', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='文章内容')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='novel.Article', verbose_name='所属文章')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='分类标题')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.CharField(max_length=255, verbose_name='评论内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.Article', verbose_name='评论文章')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novel.Comment', verbose_name='父级评论')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='标签名称')),
            ],
        ),
        migrations.AddField(
            model_name='article2tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='novel.Category', verbose_name='文章类型'),
        ),
        migrations.AlterUniqueTogether(
            name='article2tag',
            unique_together=set([('article', 'tag')]),
        ),
    ]
