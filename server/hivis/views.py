from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from seq_align import *

def index(request):
    return HttpResponse("Hello, world. You're at the HIVIS index.")

def alignment(request):
    resultdata = {"ref":1, "query":2}
    context = {'resultdata': resultdata}
    return render(request, 'hivis/alignment.html', context)

def test_alignment(request):
	args = {'name':'Dr_roboto', 'input':'>reference_seqreference_seqreference_seqreference_seq,YOURMOTHERASAHAMPSTERYOURMOTHERASAHAMPSTERYOURMOTHERASAHAMPSTERYOURMOTHERASAHAMPSTERYOURMOTHERASAHAMPSTER,>query_seq,YOURMOTHEERWASAMPSTERYOURMOTHEERWASAMPSTERYOURMOTHEERWASAMPSTERYOURMOTHEERWASAMPSTERYOURMOTHEERWASAMPSTER,>query_seq2,YOURMOTHEEASAMPSTERYOURMOTHEEASAMPSTERYOURMOTHEEASAMPSTERYOURMOTHEEASAMPSTERYOURMOTHEEASAMPSTER'}
	muscle_path = '/Users/Admin/Dropbox/Programs/tools/HIVis/serverH/serverH/server/hivis/programs/muscle3.8.31_i86darwin64'
	temp_files = '/Users/Admin/Dropbox/Programs/tools/HIVis/serverH/serverH/server/hivis/temp/'
	input_to_fasta(args['input'], args['name'], temp_files)
	muscle_align(args['name'], muscle_path, temp_files)
	temp_dict = aln_to_dict(temp_files + args['name'])
	extrainfo = {'reference_seqreference_seqrefere':"1","query_seq":"1","query_seq2":"1"}
	some_start = "1"
	out_put_test = dict_to_json(temp_dict, extrainfo, some_start)
	save_json(dict_to_json(temp_dict, extrainfo, some_start), temp_files, args['name'])
	return HttpResponse(dict_to_json(temp_dict, extrainfo, some_start))
	

	