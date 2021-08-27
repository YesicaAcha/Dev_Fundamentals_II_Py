# Word Order
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    words = OrderedDict()
    for number in range(n):
        word = input()
        count = words.get(word)
        if count is None:
            count = 1
        else:
            count = count + 1
        words[word] = count
    print(len(words))
    my_lst_str = ' '.join(map(str, words.values()))
    print(my_lst_str)
