from django.contrib import admin
from .models import Post, Comment, Team, Player

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Team)
admin.site.register(Player)

