def print_hello(prefecture) :
    if prefecture.lower() == 'kanagawa':
        print 'hello kanagawa'
    else :
        print 'hello world'

prefecture = raw_input()
print_hello(prefecture)
