from structure_information import *


def read_file(file_name: str) -> str:
    """
    file_name: Enter the name of the file
    File Format: The file should contain a one line DNA sequence with "5' " in the beginning and " 3'" in the end
    Return: Return the DNA sequence as string
    """
    seq_file = open(file_name, 'r', encoding='UTF-8')
    lines = seq_file.readlines()
    return lines[0]


def process_raw_sequence(sequence: str) -> [bool, str]:
    """
    1. Input the raw sequence read from the file
    2. Capitalize all the letters
    3. Check whether the sequence is valid (A,T,C,G)
    4. Output the pure sequence in 5 to 3 direction
    """
    sequence_out = sequence[3:-3]
    sequence_out = sequence_out.upper()  # Capitalize all letters
    for i in sequence_out:
        if i not in ['A', 'T', 'C', 'G']:
            return False
    return sequence_out


def complement_and_reverse_sequence(sequence: str) -> str:
    """
    1. Complement the input strand first. 3 -> 5 direction
    2. Reverse the complemented strand so that the strand right now is in 5 -> 3 direction
    3. Output the result strand after complementing and reversing
    """

    complement_seq = ''
    for i in sequence:
        complement_seq += DNA_complementary[i]
    reverse_complement_seq = ''
    for i in complement_seq:
        reverse_complement_seq = i + reverse_complement_seq

    return reverse_complement_seq


def six_open_reading_frames(sequence: str) -> list:
    """
    For a given sequence, there should be 6 open reading frame in total. 3 orf in normal direction, and 3 orf in
    the complement strand. However, all 6 orfs should be read in 5 to 3 direction.

    Return: All 6 possible orfs in 5-xxxxxxx-3 direction.
    """
    orf_1 = sequence[0:]  # open reading frame that start at 1st base
    orf_2 = sequence[1:]  # open reading frame that start at 2nd base
    orf_3 = sequence[2:]  # open reading frame that start at 3rd base
    reverse_complement_sequence = complement_and_reverse_sequence(sequence)  # complemented seq in 5->3 direction
    orf_4 = reverse_complement_sequence[0:]
    orf_5 = reverse_complement_sequence[1:]
    orf_6 = reverse_complement_sequence[2:]

    reading_frame_list = [orf_1, orf_2, orf_3, orf_4, orf_5, orf_6]

    return reading_frame_list


def gene_finder(sequence: str) -> str:
    """
    Identify the longest possible "gene" from a DNA sequence.

    Principle: A gene always has a start codon and a stop codon.

    Methods:
        1. Find the 1st ATG (start codon) in the open reading frame, representing the start of a gene.
        2. Identify the TAA,TAG,TGA codon after this start codon, meaning the end of a gene.
        3. The sequence between the ATG (include ATG) and the stop codon should be the sequence of a gene.
        4. Identify the if there is a 2nd ATG after the 1st ATG. If there is, repeat step 1 to 3.
        5. Return the longest gene sequence
    """
    gene_sequence_list = []
    gene_sequence = ''
    for i in range(0, len(sequence) - 2, 3):
        three_bases = sequence[i:i + 3]
        if three_bases == 'ATG':
            for j in range(i, len(sequence) - 2, 3):
                three_bases_2 = sequence[j:j + 3]
                if three_bases_2 not in ['TGA', 'TAA', 'TAG']:
                    gene_sequence += three_bases_2
                else:
                    gene_sequence += three_bases_2
                    gene_sequence_list.append(gene_sequence)
                    gene_sequence = ''
                    break
    if gene_sequence_list:
        return max(gene_sequence_list, key = len)


def six_orfs_genes(six_orfs: list) -> list:
    """
    Use gene_finder function to identify possible genes in the six open reading frames.

    Return: a list of possible gene
    """
    all_genes_list = []
    for i in six_orfs:
        all_genes_list.append(gene_finder(i))

    all_genes_list = list(filter(None, all_genes_list))
    return all_genes_list


def transcription(seq: str):
    """
    Simply replace 'T' to 'U' in the coding strand sequence would transcript the gene.

    The input should be a DNA sequence.
    """
    return seq.replace('T', 'U')


def translation(seq: str):
    """
    Use the codon table in the structure_information file to convert the RNA sequences to amino acid sequence.

    The input should be a RNA sequence.
    """
    codon_seq = ''
    for i in range(0,len(seq)-2,3):
        three_base = seq[i:i + 3]
        amino_acid = Codon_table[three_base]
        codon_seq += amino_acid
    return codon_seq



