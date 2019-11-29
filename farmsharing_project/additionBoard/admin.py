from django.contrib import admin
from .models import QuestionBoard,QB_comment,DealBoard,DB_comment

admin.site.register(QuestionBoard)
admin.site.register(QB_comment)
admin.site.register(DealBoard)
admin.site.register(DB_comment)