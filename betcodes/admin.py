from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.


@admin.register(models.FootballClub)
class FootballClubAdmin(admin.ModelAdmin):
    list_display = ['club_name', 'country', 'continent', 'domestic_league', 'logo']


@admin.register(models.BetCode)
class BetCodeAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'bet', 'ht_home_score', 'ht_away_score', 'ft_home_score', 'ft_away_score', 'remark', 'match_time']

@admin.register(models.BookCodeInfo)
class BookCodeInfoAdmin(admin.ModelAdmin):
    list_display = ['book_code', 'total_odd', 'ticket_date']

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'placed_at', 'user']
    list_select_related = ['user']
