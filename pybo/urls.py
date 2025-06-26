from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    ##name 속성 추가 : URL 별칭을 사용하여 URL 리팩토링 방지
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
