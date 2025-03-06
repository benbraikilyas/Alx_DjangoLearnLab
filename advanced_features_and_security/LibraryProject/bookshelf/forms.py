from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search for a book"})
    )

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100)
