from django.contrib import admin
from video.models import VideoData, CommentData, User


# Register your models here.


@admin.register(VideoData)
class VideoDataAdmin(admin.ModelAdmin):
    list_display = ('aweme_id', 'username', 'likeCount', 'commentCount', 'description', 'publishTime')
    search_fields = ('username', 'description')
    list_filter = ('publishTime',)
    ordering = ('-publishTime',)


@admin.register(CommentData)
class CommentDataAdmin(admin.ModelAdmin):
    list_display = ('userid', 'username', 'commentTime', 'userIP', 'content', 'likeCount')
    search_fields = ('username', 'content')
    list_filter = ('commentTime',)
    ordering = ('-commentTime',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'createTime')
    search_fields = ('username',)
    list_filter = ('createTime',)
    ordering = ('-createTime',)
