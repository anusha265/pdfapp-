from django import forms

class PDFMergeForm(forms.Form):
    pdf_file = forms.FileField(label='Select PDF file')
    page_file = forms.FileField(label='Select page file')
    position = forms.IntegerField(label='Enter the position to insert the page')