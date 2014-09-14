#!/usr/bin/python


# Import required modules

import sys
import subprocess

from subprocess import call, Popen, PIPE
#import subprocess

# Required variables


#parser = argparse.ArgumentParser(description='Python sequence alignment tool with JSON output')
#parser.add_argument('-i','--input', help='input sequence', required=True)
#parser.add_argument('-n','--name', help='unique job identifier', required=True)
#args = vars(parser.parse_args())

#muscle_path = '/Users/Admin/Dropbox/Programs/tools/muscle3.8.31_i86darwin64'
#temp_files = '/Users/Admin/Dropbox/Programs/tools/HIVis/H/Python/'


# Define required functions

def input_to_fasta(input_seq, out_name, temp_files):
	"Saves the input sequence as a fasta file"
	split_in_seq = input_seq.split(',')
	fast_out = open((temp_files + out_name + '.fa'), 'w')
	print split_in_seq
	for line in split_in_seq:
		fast_out.write(line + '\n')
	fast_out.close()

		
def muscle_align(output_name, muscle_path, temp_files):
	"Aligns two sequences"
	# Add description of the output
	raw_alignment = subprocess.Popen([muscle_path, "-in", (temp_files + output_name + '.fa'), '-clwout', (temp_files + output_name + '.aln')], stdout=PIPE)
	raw_alignment.wait()
	muscle_alignment_result = raw_alignment.stdout.read()
	return muscle_alignment_result
	

def aln_to_dict(input_aln_file):
	"Convert an aln file to a python dict"
	
	aln_file = open((input_aln_file  + '.aln'), "r")
	
	aln_dict = {}
	
	# Split the sequences into the dict
	for line in aln_file:
		if line[0] != '\n' and line[0:6] != 'MUSCLE' and line[0] != ' ':
			line_list = line.split()
			aln_dict[line_list[0]] = ''
			
	aln_file = open((input_aln_file  + '.aln'), "r")
	
	for line in aln_file:
		if line[0] != '\n' and line[0:6] != 'MUSCLE' and line[0] != ' ':
			line_list = line.split()
			seq = aln_dict[line_list[0]] + line_list[1]
			aln_dict[line_list[0]] = seq
			
	return aln_dict

def dict_to_json(proc_dict, info_dict, aln_start):
	"Convert a processed python dict to the JSON output"
	json_string = ''
	headder_string = '{"header":'
	names_string = '{"names": ['
	starts_string = '"starts": ['
	alignment_start_string = '"alignment_start": ' + aln_start + '},'
	alignment_string = ''
	
	for key in proc_dict:
		names_string = names_string + '"' + key + '",'
		starts_string = starts_string + '"' + info_dict[key] + '",'
	
	names_string = names_string[:-1] + '],'
	starts_string = starts_string[:-1] + '],'
	#print headder_string, names_string, starts_string, alignment_start_string
	
	
	for key in proc_dict:
		aln_length = len(proc_dict[key])
	
	i = 0
	while i < aln_length:
		align_line = '['
		for key in proc_dict:
			align_line = align_line + '"' + proc_dict[key][i] + '",'
		
		i = i + 1
		align_line = align_line[:-1] + '],'
		alignment_string = alignment_string + align_line
	alignment_string = alignment_string[:-1]

	json_string = headder_string + names_string + starts_string + alignment_start_string + '"alignment": [' + alignment_string + ']}'
	return json_string


