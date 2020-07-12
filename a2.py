def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0;

    for nuc in dna:
        if nuc == nucleotide:
            count += 1

    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

    The dna parameter is a potential DNA sequence.
    Return True if and only if the DNA sequence is valid
    (that is, it contains characters other than ’A’, ’T’, ’C’ and ’G’).

    >>> 
    is_valid_sequence('AGCTAC')
    True
    >>> is_valid_sequence('AGC')
    True
    >>> is_valid_sequence('AGCZ')
    False
    >>> is_valid_sequence('AGc')
    False
    """

    dna_characters = 'ATCG'

    for char in dna:
        if not char in dna_characters:
            return False

    return True


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    ​The dna1 and dna2 parameters are the first two DNA sequences
    and the third parameter is an index.
    Return the DNA sequence obtained by inserting
    the second DNA sequence into the first DNA sequence at the given index.

    Precondition: index >= 0
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    """

    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nuc):
    """ (str) -> str

    The parameter nuc is a nucleotide ('A', 'T', 'C' or 'G').
    Return the nucleotide's complement. 

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """

    if nuc == 'A' or nuc == 'T':
        return 'T' if nuc == 'A' else 'A'

    if nuc == 'C' or nuc == 'G':
        return 'G' if nuc == 'C' else 'C'


def get_complementary_sequence(dna):
    """ (str) -> str

    The dna parameter is a DNA sequence.
    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CG')
    'GC'
    >>> get_complementary_sequence('ACGTACG')
    'TGCATGC'
    """

    complementary_dna = ''

    for nucleotide in dna:
        complementary_dna += get_complement(nucleotide)

    return complementary_dna

