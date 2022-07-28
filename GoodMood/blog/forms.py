from django import forms
from django.contrib.auth.models import User

from .models import *


# class AddCommentForm(forms.ModelForm):
#     # автоматическое заполнение юзера в комментариях, сработает после авторизации
#     def __init__(self, *args, **kwargs):
#         super().__init__(args, kwargs)
#         self.fields['person_comment'].queryset = User.objects.filter(name=self.)
#
#     class Meta:
#         model = Comment
#         fields = ['title', 'content', 'is_published', 'person_comment']
# class AddRecords(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     #     self.fields['cat'].empty_label = 'Категория не выбрана'
#
#     class Meta:
#         model = Records
#         fields = ['title', ['record_closed'], ['person_record'], ['service']]
