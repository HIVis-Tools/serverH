from django import forms


class Alignment_form(forms.Form):
	HXB2_SEQUENCES = (
		('env', 'Env'),
		('gag', 'Gag'),
		('nef', 'Nef'),
		('pol', 'Pol'),
		('rev', 'Rev'),
		('tat', 'Tat'),
		('vif', 'Vif'),
		('vpr', 'Vpr'),
		('vpu', 'Vpu'),
		('other', 'Other'),
	)		
	fasta_string = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
	user_name = forms.CharField(max_length=24)
	protein_choice = forms.ChoiceField(choices=HXB2_SEQUENCES)

	
	def __init__(self, request, *args, **kwargs):
		super(Alignment_form, self).__init__(*args, **kwargs)
		
class Additional_form(forms.Form):
	ref_string = forms.CharField(widget=forms.Textarea)

	def __init__(self, request, *args, **kwargs):
		super(Additional_form, self).__init__(*args, **kwargs)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
