import sys
from function_kit import *


def main():
    file_name = sys.argv[1:][0]  # read file from command line
    original_sequence = read_file(file_name)

    DNA_sequence = process_raw_sequence(original_sequence)  # validate the sequence
    six_orfs = six_open_reading_frames(DNA_sequence)  # find the six open reading frames of the given sequence
    possible_gene_list = six_orfs_genes(six_orfs)  # find the possible gene DNA sequence

    longest_gene_dna = max(possible_gene_list)  # longest DNA sequence
    longest_gene_rna = transcription(longest_gene_dna)  # longest DNA sequence transcript to RNA sequence
    longest_gene_aa = translation(longest_gene_rna)  # longest DNA sequence translate to amino acid sequence

    print()
    print('The input sequence is: ', DNA_sequence)
    print()
    print('After analyzing all the six open reading frames, the DNA sequence of the longest possible gene is:')
    print(longest_gene_dna)
    print()
    print('The mRNA sequence of the gene is:')
    print(longest_gene_rna)
    print()
    print('The protein sequence of the gene is:')
    print(longest_gene_aa)

    f = open('Results/results_'+file_name,'w')
    f.write('The file is the result of the gene finder program on ' + file_name + '\n')
    f.write('\n')
    f.write('The DNA sequence of longest possible gene is: ' + longest_gene_dna + '\n')
    f.write('The mRNA sequence of the gene is: '+ longest_gene_rna + '\n')
    f.write('The protein sequence of the gene is: ' + longest_gene_aa + '\n')

main()
