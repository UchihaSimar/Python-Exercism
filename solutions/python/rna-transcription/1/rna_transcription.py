def to_rna(dna_strand):
    result = ""
    for dna_strand_char in dna_strand:
        if dna_strand_char == 'G':
            result = result + 'C'
        if dna_strand_char == 'C':
            result = result + 'G'
        if dna_strand_char == 'T':
            result = result + 'A'
        if dna_strand_char == 'A':
            result = result + 'U'

    return result
            
