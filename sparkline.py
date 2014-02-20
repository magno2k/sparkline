#!/usr/bin/env python

import sys
import os

def main():

	argc = len ( sys.argv )
	if sys.stdin.isatty() and argc < 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print "Sparklines"
		print "Usage: %s [number] [number] [number] ..\n" % sys.argv[0]
		
	valor = []
	DBL_MAX = sys.float_info.max
	DBL_MIN = sys.float_info.min
	max_=0
	min_=0
	total = 0

	if ( argc > 1 ):
		total = argc - 1

		for i in range (total):
			valor.append(float(sys.argv[i+1]))
			if valor[i] > DBL_MAX:
				max_ = valor[i]
			elif valor[i] < DBL_MIN:
				min_ = valor[i]

	diferenca = max_ - min_ + 1
	if diferenca < 1:
		diferenca = 1
	level = 2
	for x in range (total):
		sys.stdout.write(unichr(ord ('\xe2')))
		sys.stdout.write(unichr(ord ('\x96')))
		sys.stdout.write(unichr(ord ('\x81') +  int ( round ( valor[x] - min_ + 1 ))  / (diferenca * (level - 1))))
		
	print '\n'


if __name__ == "__main__":

	main()
  
  
  
