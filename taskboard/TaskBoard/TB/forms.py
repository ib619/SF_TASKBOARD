from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article, Response
from .choices import DECISION_TYPE_IN_FORM



class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = ['title', 'category', 'text', 'video', 'video2']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']


class DecisionForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['decision']

    def __init__(self, *args, **kwargs):
        super(DecisionForm, self).__init__(*args, **kwargs)
        self.fields['decision'].choices = DECISION_TYPE_IN_FORM


