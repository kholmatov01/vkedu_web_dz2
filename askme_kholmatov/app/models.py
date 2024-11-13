from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    avatar = models.ImageField

class Tag(models.Model):
    tag = models.CharField(max_length=30)

class Question(models.Model):
    user = models.ForeignKey(settings.USER_AUTH_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('s', 'Solved')
        ('ns', 'Not Solved')
    ]
    status = models.CharField()
    tag = models.ManyToManyField(Tag)


class Answer(models.Model):
    user = models.ForeignKey(settings.USER_AUTH_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField()
    

class QuestionLike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("question", "user")

class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("answer", "user")
