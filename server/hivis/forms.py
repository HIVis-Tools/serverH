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

        user_name = forms.CharField(label='Username', max_length=20,  widget=forms.TextInput(attrs={'class' : 'username_input'}))
        fasta_string = forms.CharField(label='\nFasta sequence', widget=forms.Textarea(attrs={'class' : 'out-box'}))
	protein_choice = forms.ChoiceField(required=False, choices=HXB2_SEQUENCES, widget=forms.Select(attrs={'class' : 'select-box'}))
#        protein_choice = forms.ChoiceField(label='\nReference Sequence', choices=HXB2_SEQUENCES)
	
	def __init__(self, request, *args, **kwargs):
		super(Alignment_form, self).__init__(*args, **kwargs)
		
class Additional_form(forms.Form):
	ref_string = forms.CharField(label='',widget=forms.Textarea(attrs={'class' : 'out-box'}))

	def __init__(self, request, *args, **kwargs):
		super(Additional_form, self).__init__(*args, **kwargs)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
