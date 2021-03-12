from django import forms
from .models import Boards, Topics, Posts


class BoardForm(forms.ModelForm):
    class Meta:
        model = Boards
        fields = ('__all__')

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ('__all__')