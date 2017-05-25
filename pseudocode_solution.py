if op == '+':

    func = add

elif op == '*':

    func = multiply


try:
    print func(n1, n2)
except NameError:
    print 'invalid number of arguments'
