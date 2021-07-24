def str_to_lits(payload:str) -> [] :
    strs = []
    for char in payload :
        if char.isalnum():
            strs.append(char.lower())
    return strs

def isPalindrome(ls: []) -> bool:
    while len(ls) > 1:
        if ls.pop(0) != ls.pop():
            return False
        else:return True
    #return [i for i in ls if ls.pop(0) ! = ls.pop()]

if __name__ == '__main__':
    ls = str_to_lits("A man, a plan, a canal: Panama")
    print(ls)
    ispal = isPalindrome(ls)
    print(ispal)


