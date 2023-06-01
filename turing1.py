from typing import List

def solution(a, b):
    cant = a.count(b*2) * 2 
    return cant



assert solution("popokpo", "po") == 2
assert solution("pokakapokapo", "ka") == 2
