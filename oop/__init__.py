if __name__ == '__main__':
    ls = ['exit', 'add', 'print', 'delete']
    t = ''
    for i, j in enumerate(ls):
        t += str(i) + '-' + j + '\t'
    print(t)