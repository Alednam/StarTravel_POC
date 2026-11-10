from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(
        label='Enter your scientific query or equation',
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'query-input', 'placeholder': 'e.g., "reality observer" or "2*x + 5" or "(A & B) >> C"'})
    )

class UploadTheoryForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(label="Upload Markdown Theory (.md)")
