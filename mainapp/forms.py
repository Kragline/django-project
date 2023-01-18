from django import forms
from .models import Post, Category


#name is the "name" field from Catrgory model in models.py file
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('image', 'category', 'author', 'content')
        
        widgets = {
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'value' : '','id': 'user',  'type' : 'hidden'}),
            'category' : forms.Select(choices=choice_list, attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Description or some text...'}),
        }


class EditForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('image', 'category', 'content')
        
        widgets = {
            'category' : forms.Select(choices=choice_list, attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Description or some text...'}),
        }