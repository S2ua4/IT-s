
from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    ##앱 전용 URL과 앱별 URL을 구분하여 관리할 것 => 독립성 강화
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), #pybo/로 시작하는 페이지 -> 해당 파일의 매핑 정보를 읽어서 처리
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
