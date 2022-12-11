from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        "Group",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        # выводим текст поста 
        return self.text
        
    class Meta:
        ordering = ['-pub_date']
        default_related_name = 'posts'


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title



