def str_to_list(payload:str) -> []:
    return [i for i in payload if i.isalnum()]

def reverse_string(ls:[]) -> str:
    '''left, right = 0, len(ls) -1
    while left < right:
        ls[left], ls[right], = ls[right], ls[left]
        ls[left]: ls[right], = ls[right]:ls[left]
        left += 1
        right -= 1'''
    return ls[::-1]

def list_to_str(ls) -> str:
    return "".join([i for i in ls])

def total(payload) -> str:
    return "".join([i for i in [i.lower() for i in payload if i.isalnum()][::-1]])


if __name__ == '__main__':
    ls = str_to_list(input("input"))
    str_ls = list_to_str(reverse_string(ls))
    print(str_ls)
    print(reverse_string(ls))