def farts(n: int) -> str:
    print('why don\'t you love me, number {}?'.format(n))
    a = 10
    if n > 5:
        return 'cats'
    else:
        return a

b = farts(1)
c = farts(10)

d = farts('Bob')

e = farts(farts)
