from django import forms
from .models import Stock
from dal import autocomplete

class StockForm(forms.Form):
    stock = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='stock_autocomplete',
            attrs={
                'data-placeholder': 'Select a stock..'
            }
        )
    )
