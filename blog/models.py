from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    title = models.CharField(max_length=200, help_text='не боле 200 символов', db_index=True)
    content = RichTextField(max_length=5000, blank=True, null=True, help_text='не боле 5000 символов')
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # в url при использовании slug обязятельно добавлять id + get_absolute_url()
    slug = models.SlugField(max_length=50) # unique=True
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True)
    reply = models.ForeignKey('self', null=True, related_name='reply_ok', on_delete=models.CASCADE)


    def total_likes(self):
        return self.likes.count()


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

    def __str__(self):
        return self.title
