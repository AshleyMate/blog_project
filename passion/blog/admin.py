from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  # Post 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지 정의하는 클래스
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}