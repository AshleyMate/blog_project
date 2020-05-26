from django.urls import path
from bookmark import views

app_name = 'bookmark'
# app_name은 애플리케이션 이름공간(namespace)을 'bookmark'로 지정해준 것. 애플리케이션 네임스페이스는 URL 패턴의 이름을 정하는데 사용됨

urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    # URL 패턴 이름은 app_name을 포함한 'bookmark:index'가 된다.
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    # URL 패턴 이름은 app_name을 포함한 'bookmark:detail'이 된다.
    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),

]
