from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from seq_align import *
from hivis import forms
import uuid
import os

def index(request):
#    return HttpResponse("Hello, world. You're at the HIVIS index.")
	context = {}
	return render(request, 'hivis/index.html', context)


def alignment(request):
    resultdata = {"ref":1, "query":2}
    context = {'resultdata': resultdata}
    return render(request, 'hivis/alignment.html', context)

def test_alignment(request):
	# Input formatting
	fasta_string = request.POST.get('fasta_string', False)
	user_name = request.POST.get('user_name', False)
	protein_choice = request.POST.get('protein_choice', False)
	user_name = user_name.replace(' ','_')
	job_id = user_name + str(uuid.uuid4())[-6:]
	
	# Selecting the ref seq
	if protein_choice != 'other':
		ref_seq_path = './hivis/static/HXB2_ref_seq/' + protein_choice + '.fasta'
		ref_seq_file = open(ref_seq_path, 'r')
		ref_seq = ref_seq_file.read()
	
	else:
		ref_seq = request.POST.get('ref_string', False)
	
	# Variable setting
	temp_files = './hivis/static/temp/' + job_id + '/'
	os.system('mkdir ' + temp_files)
	muscle_path = './hivis/programs/muscle3.8.31_i86darwin64'
	
	# Write to file
	fasta_output = open(temp_files + job_id + '.fa', 'w')
	fasta_string = ref_seq + '\n' + fasta_string
	fasta_output.write(fasta_string)
	fasta_output.close()
	e = muscle_align(job_id, muscle_path, temp_files)
	
	temp_dict = aln_to_dict(temp_files + job_id)
	
	out_put_test = dict_to_json(temp_dict)
	save_json(dict_to_json(temp_dict), temp_files, job_id)
	#return HttpResponse(job_id)
	
	resultdata = {"ref":job_id, "query":2}
	context = {'resultdata': resultdata}
	return render(request, "hivis/display_page.html", context)
	

def pretty_input_page(request):
	newForm = forms.Alignment_form(request)
	hidden_form = forms.Additional_form(request)
	hidden_upload_form = forms.UploadFileForm(request)
	context = {}
	context['form'] = newForm
	context['hidden_form'] = hidden_form
	context['hidden_upload_form'] = hidden_upload_form
	return render(request, "hivis/pretty_input_page.html", context)
