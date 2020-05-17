from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'
# app_name은 애플리케이션 이름공간(namespace)을 'bookmark'로 지정해준 것. 애플리케이션 네임스페이스는 URL 패턴의 이름을 정하는데 사용됨

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    # URL 패턴 이름은 app_name을 포함한 'bookmark:index'가 된다.
    path('<int:pk>', BookmarkDV.as_view(), name='detail'),
    # URL 패턴 이름은 app_name을 포함한 'bookmark:detail'이 된다.

]
