from django.contrib import admin
from .models import QuestionBoard,QB_comment,DealBoard

admin.site.register(QuestionBoard)
admin.site.register(QB_comment)
admin.site.register(DealBoard)