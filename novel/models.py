from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInfo(AbstractUser):
    nid = models.BigAutoField(primary_key=True)
    nickname = models.CharField( max_length=32)
    avatar = models.ImageField(default='', upload_to="user/%Y/%m", verbose_name='头像')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.username


class ArticleDetail(models.Model):
    '''
        文章状态:已完结，连载
        作者
        分类
        更新时间
        文章字数
        标题
        图片
    '''
    nid = models.AutoField(primary_key=True, default=1)
    content = models.TextField(verbose_name='文章内容', )
    article = models.OneToOneField(verbose_name='所属文章', to='Article', to_field='nid')



class Article(models.Model):
    nid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述')
    avatar = models.ImageField(default='', upload_to="article/%Y/%m", verbose_name='头像')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    category = models.ForeignKey(verbose_name='文章类型', to='Category', to_field='nid', null=True)


class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)


class Article2Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid')
    tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='nid')

    class Meta:
        unique_together = [
            ('article', 'tag'),
        ]


class Category(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)


class Comment(models.Model):
    nid = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    parent_id = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')
    content = models.CharField(verbose_name='评论内容', max_length=255)
    article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='nid')
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid')


class Directory(models.Model):
    pass


class Poll(models.Model):
    '''
    投票数
    '''



