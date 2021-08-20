def params(a, b, c, *args, **kw):
    print(args)
    print(kw)
    return args[0] + kw['e']


print(params(1, 2, 3, 4, 5, 6, e=999, name='lisi'))
