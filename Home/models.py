from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=30)
    win_record = models.PositiveIntegerField(default=0)
    lost_record = models.PositiveIntegerField(default=0)
    percent_record = models.PositiveIntegerField(default=0)

    def computing_record(self):
        wins = self.win_record
        lost = self.lost_record
        if wins > 0:
            self.percent_record = int(wins / (wins + lost) * 100)
            self.save()

    def __str__(self):
        return self.user.username


# class PostModel(models.Model):
#     text = models.TextField()
#     age = models.IntegerField()
#     time = models.DateTimeField(auto_now_add=True)
#     detail = models.TextField(null=True)
#
#     def __str__(self):
#         return self.text
#
#     def get_absolute_url(self):
#         # return f'/detail/{self.id}'
#         return reverse('Game:detail', args=[str(self.id)])
