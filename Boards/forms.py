from django import forms
from .models import Boards, Topics, Posts


class BoardForm(forms.ModelForm):
    class Meta:
        model = Boards
        fields = ('__all__')

class TopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'placeholder' : "Write what's in your brain...!"
    }), max_length=4000, help_text='Max length of this field is 4000 character.')
    class Meta:
        model = Topics
        fields = ('subject','message')