from django import forms
from .models import CompressImage

class CompressImageForm(forms.ModelForm):
    class Meta:
        model = CompressImage
        fields = ('original_img', 'quality')
        
    original_img = forms.ImageField(label='upload an Image')