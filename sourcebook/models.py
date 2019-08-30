from django.db import models


class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)

    def __str__(self):
        return self.name

class Page(models.Model):
    """ページ"""
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='book', on_delete=models.CASCADE)
    name = models.CharField('ページ名', max_length=255)

    def __str__(self):
        return self.name

class Source(models.Model):
    """ソースコード等"""
    page = models.ForeignKey(Page, verbose_name='ページ', related_name='page', on_delete=models.CASCADE)
    text = models.TextField('テキストエリア', blank=True)
    text_flg = models.IntegerField('テキストフラグ')

    def __str__(self):
        return self.text

# Create your models here.
