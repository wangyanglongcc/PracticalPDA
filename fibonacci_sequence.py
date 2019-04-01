
def fib(x):
    assert isinstance(x,int),'请输入一个正整数'
    fiba = lambda x:1 if x<=2 else fiba(x-1) + fiba(x-2)
    return fiba(x)

if __name__ == '__main__':
    '112358....'
    print(fib(6))
