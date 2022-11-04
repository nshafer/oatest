from django.db import models


class Article(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
