from django.db import models

class Question(models.Model) :
    subject = models.CharField(max_length=200) #글자수가 제한된 텍스트
    content = models.TextField() #글자수가 제한되지 않은 텍스트
    create_date = models.DateTimeField() #날짜와 시간 정보를 저장

    def __str__(self):
        return self.subject

class Answer(models.Model):
    #기존 모델을 해당 클래스의 속성으로 연결 시 ForeginKey 사용 + 연쇄삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

