import random


def eeee(a):
    if type(a) == tuple and len(a) > 1:
        args = [eeee(x) for x in a[1:]]
        return a[0](*args)
    else:
        return a

def oooo(*code, **symbols):
    if len(code) > 1:
        args = []
        for x in code[1:]:
            try:
                x1 = symbols[x]
            except Exception:
                x1 = x
            args.append(oooo(x1, **symbols))
        print(args)
        return code[0](*args)
    else:
        return code


print(eeee(
    (str.format, 'hello my name is {}',
     (str.format, '{}{}{}','b', 'o', 'b'))
))

print(oooo(
    str.format, 'hello my name is {}', 'a',
    a='bob'
))
