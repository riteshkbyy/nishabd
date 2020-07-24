from django import forms
from .models import Article, CATEGORY
class ArticleForm(forms.ModelForm):
    category= forms.ChoiceField(choices=CATEGORY)
    class Meta:
        model = Article
        fields = [ "category", "title","content","article_image","article_image2"]
   