from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_public = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)
