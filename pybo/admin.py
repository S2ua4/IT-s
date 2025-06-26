from django.contrib import admin
from pybo.models import Question, Answer

##Question 모델에 세부 기능을 추가할 수 있는 클래스 생성
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] #제목 검색

##장고 관리자 화면에서 모델 관리 가능
admin.site.register(Question, QuestionAdmin) #Question 모델 등록
admin.site.register(Answer)

