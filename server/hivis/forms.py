from django import forms

class Alignment_form(forms.Form):		
	fasta_string = forms.CharField(widget=forms.Textarea)
	user_name = forms.CharField(max_length=24)
	
	def __init__(self, request, *args, **kwargs):
		super(Alignment_form, self).__init__(*args, **kwargs)