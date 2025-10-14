def to_rna(dna_strand):
    to_rna=""
    for item in dna_strand:
        if item=='G':
            to_rna=to_rna+'C'
        elif item=='C':
            to_rna=to_rna+'G'
        elif item=='T':
            to_rna=to_rna+'A'
        elif item=='A':
            to_rna=to_rna+'U'
        else:
            raise ValueError("Is not a DNA strand")
    return to_rna
        