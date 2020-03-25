from django import forms 

class SearchForm(forms.Form):
    query = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class' : 'mr-sm-2 form-control',
                'type':'search',
                'aria-label': 'Search'
        }))