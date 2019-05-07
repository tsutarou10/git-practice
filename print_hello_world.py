#coding: utf-8

def print_hello(prefecture) :
    prefecture = prefecture.lower()
    if prefecture == 'kanagawa':
        print('hello kanagawa')
    elif prefecture == 'tokyo':
        print('hello tokyo')
    else :
        print('hello world')

if __name__ == '__main__':
    prefecture = input()
    print_hello(prefecture)
