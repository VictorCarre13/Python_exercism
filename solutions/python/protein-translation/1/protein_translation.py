def proteins(strand):
    result=[]
    count = 0
    codon=""
    for item in strand:
        if count <3:
            codon=codon + item.upper()
            count+=1
            print(codon)
        else:
            codon=""
            count = 1
            codon+=item.upper()
        if codon in ['UAA','UAG','UGA']:
            return result
        if codon == 'AUG':
            result.append('Methionine')
        if codon in ['UUU', 'UUC']:
            result.append('Phenylalanine')
        if codon in ['UUA', 'UUG']:
            result.append('Leucine')
        if codon in ['UCU', 'UCC', 'UCA', 'UCG']:
            result.append('Serine')
        if codon in ['UAU', 'UAC']:
            result.append('Tyrosine')
        if codon in ['UGU', 'UGC']:
            result.append('Cysteine')
        if codon == "UGG":
            result.append('Tryptophan')
    return result