from collections import Counter

def count_dup(cadena):
    return len([s for s in list(Counter(cadena.lower()).most_common()) if s[1] > 1])



assert count_dup("abcde") == 0
assert count_dup("aabbcde" ) == 2
assert count_dup("aabBcde") == 2
assert count_dup("indivisibility") == 1
assert count_dup("Indivisibilities") == 2
assert count_dup("aA11") == 2
assert count_dup("ABBA") == 2


def remove_uniq(cadena):
    return ''.join([c for c in cadena if cadena.count(c) > 1])




assert remove_uniq("abccdefee") == "cceee"

