def find_anagrams(word, candidates):
    """Find candidates that are valid anagrams of the target word.

    :param word: str - target word
    :param candidates: list[str] - candidate words to test
    :return: list[str] - list of candidates that are anagrams (preserving original casing)
    """
    target_lower = word.lower()
    target_sorted = sorted(target_lower)
    anagrams = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        
        # 1. A word is NOT an anagram of itself (case-insensitive)
        if candidate_lower == target_lower:
            continue
            
        # 2. Check if letter counts match
        if sorted(candidate_lower) == target_sorted:
            anagrams.append(candidate)

    return anagrams