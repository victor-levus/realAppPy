from email.policy import default
from multiprocessing import managers
from django.conf import settings
from django.db import models

# Create your models here.


class FootballClub(models.Model):
    club_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True, blank=True)
    continent = models.CharField(max_length=255, null=True, blank=True)
    domestic_league = models.CharField(max_length=255, null=True, blank=True)
    logo = models.TextField(null=True, blank=True)


class BetCode(models.Model):
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    bet = models.CharField(max_length=255)
    odd = models.DecimalField(max_digits=6, decimal_places=2)
    ht_home_score = models.IntegerField(null=True, blank=True)
    ht_away_score = models.IntegerField(null=True, blank=True)
    ft_home_score = models.IntegerField(null=True, blank=True)
    ft_away_score = models.IntegerField(null=True, blank=True)
    remark = models.BooleanField()
    match_time = models.DateTimeField(null=True)
    placed_at = models.DateTimeField(auto_now=True)


class BookCodeInfo(models.Model):
    book_code = models.CharField(max_length=255)
    total_odd = models.DecimalField(max_digits=6, decimal_places=2)
    ticket_date = models.DateTimeField()
    placed_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # image = models.ImageField(null=True, blank=True)
    placed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    description = models.TextField()
    placed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replys')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    description = models.TextField()
    placed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Likes(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)
    placed_at = models.DateTimeField(auto_now_add=True)
