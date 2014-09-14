from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from seq_align import *
from hivis import forms
import uuid
import os

def index(request):
    return HttpResponse("Hello, world. You're at the HIVIS index.")

def alignment(request):
    resultdata = {"ref":1, "query":2}
    context = {'resultdata': resultdata}
    return render(request, 'hivis/alignment.html', context)

def test_alignment(request):
	fasta_string = request.POST.get('fasta_string', False)
	user_name = request.POST.get('user_name', False)
	user_name = user_name.replace(' ','_')
	job_id = user_name + str(uuid.uuid4())[-6:]
	
	temp_files = '/Users/Admin/Dropbox/Programs/tools/HIVis/serverH/serverH/server/hivis/temp/' + job_id + '/'
	os.system('mkdir ' + temp_files)
	
	muscle_path = '/Users/Admin/Dropbox/Programs/tools/HIVis/serverH/serverH/server/hivis/programs/muscle3.8.31_i86darwin64'

	fasta_output = open(temp_files + job_id + '.fa', 'w')
	fasta_output.write(fasta_string)
	fasta_output.close()
	e = muscle_align(job_id, muscle_path, temp_files)
	
	temp_dict = aln_to_dict(temp_files + job_id)
	
	out_put_test = dict_to_json(temp_dict)
	save_json(dict_to_json(temp_dict), temp_files, job_id)
	return HttpResponse(request.POST.get('fasta_string', False))
	

def input_page(request):
	newForm = forms.Alignment_form(request)
	context = {}
	context['form'] = newForm
	return render(request, "hivis/input_page.html", context)