from turtle import update
from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.
class Articles(models.Model):
    author  = models.ForeignKey(get_user_model(), related_name ='articles' , on_delete= models.CASCADE )
    title =models.CharField(max_length=200)
    body = models.TextField(max_length= 600)
    likes = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add= True)
    update = models.DateTimeField(auto_now= True)
    slug  = models.SlugField(max_length=250,unique=True)


    class Meta:
        ordering = ("-created_date",)


    def __str__(self):
        return self.title[:50]

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(),related_name= "comment", on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles,related_name= 'comment', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add= True)


    class Meta:
        ordering = ("-created",)


    def __str__(self):
        return self.body[:50]



