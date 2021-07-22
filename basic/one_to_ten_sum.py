def one_to_ten_sum():
    #example 1
    sum = 0
    # for i in []:
    for i in range(1,10+1):
        sum += i

    # example 2
    sum = sum(i for i in range(1, 11))
    print(sum(i for i in range(1,20)))
    print(sum(i for i in range(1,19)))

    # example 3
    sum = sum(range(1, 11))
    print(sum)

def one_to_ten_sum_2():
    print(sum(range(1,11)))

if __name__ == '__main__':
    one_to_ten_sum()
    one_to_ten_sum_2()