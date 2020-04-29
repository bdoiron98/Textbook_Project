from django import forms
from .models import Post, Textbook

class CustomPostForm(forms.ModelForm):
    textbook = forms.ModelChoiceField(queryset=Textbook.objects.all().order_by('title'))
    # slug = CharField(validators=[validate_slug])
    # accepted_payers = forms.ModelMultipleChoiceField(queryset=Payer.objects.all(),
                      # widget=forms.CheckboxSelectMultiple(attrs={'class':'nobullet'}),required=False)

    class Meta:
        model = Post
        fields = ['new', 'body', 'textbook', 'price']
