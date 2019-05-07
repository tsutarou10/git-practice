def print_hello(prefecture) :
    prefecture = prefecture.lower()
    if prefecture == 'kanagawa':
        print 'hello kanagawa'
    elif prefecture == 'tokyo':
        print 'hello tokyo'
    else :
        print 'hello world'

prefecture = raw_input()
print_hello(prefecture)
