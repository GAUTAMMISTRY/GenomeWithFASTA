def main(file):
	#Reading Fasta file
	f=open('dna2.fasta','r')

	seqs={}
	for line in f:
		line=line.rstrip()   
		# distinguish header from sequenceif 
		if line[0]=='>': # or line.startswith('>')	
			words=line.split()
			name=words[0][1:]
			seqs[name]=''
		else : 
			# sequence, not 
			seqs[name] = seqs[name] + line

	LengthOfSequence=[]
	AATGGCAOc=[]
	CGCGCCGOc=[]
	TGCGCGCOc=[]
	CATCGCCOc=[]
	for name,seq in seqs.items():
		LengthOfSequence.append(len(seq))
		AATGGCAOc.append(seq.count('AATGGCA'))
		CGCGCCGOc.append(seq.count('CGCGCCG'))
		TGCGCGCOc.append(seq.count('TGCGCGC'))
		CATCGCCOc.append(seq.count('CATCGCC'))
		CATCGCCOc.append(seq.count('ATGCCCTAG'))


	print('Total DNA Lengths {}'.format( sorted(LengthOfSequence)))
	print('AATGGCA {}'.format(sorted(AATGGCAOc)))
	print('CGCGCCGOc {}'.format(sorted(CGCGCCGOc)))
	print('TGCGCGCOc {}'.format(sorted(TGCGCGCOc)))
	print('CATCGCCOc {}'.format(sorted(CATCGCCOc)))


if __name__ == "__main__":
    main()
