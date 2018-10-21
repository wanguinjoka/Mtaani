from .models import News

class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['author','date_posted']
        widgets = {
            'kijiji': forms.CheckboxSelectMultiple(),
        }
