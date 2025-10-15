def find_anagrams(word, candidates):
    return [c for index, c in enumerate(candidates) if sorted(word.lower()) == sorted(c.lower()) and word.lower() != c.lower()]