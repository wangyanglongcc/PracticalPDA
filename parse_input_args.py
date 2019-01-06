# -*- coding: UTF-8 -*-
import sys
import argparse

def parse_input_args():
	if len(sys.argv) == 1:
		sys.argv.append('-h')
	parser = argparse.ArgumentParser()
	parser.add_argument('-c',dest = 'goodscode')
	parser.add_argument('-d',dest = 'date')
	parser.add_argument('-o',dest = 'output_path')
	args = vars(parser.parse_args())
	return args['goodscode'],args['date'],args['output_path']
def main(goodscode,date,output_path):
	print('-'*30 + 'start' + '-'*30)
	print(goodscode,date,output_path)

if __name__ == '__main__':
	goodscode,date,output_path = parse_input_args()
	main(goodscode,date,output_path)
