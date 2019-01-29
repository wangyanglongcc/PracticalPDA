#　使用sys模块下的getsizeof函数获取，单位为字节（Byte)
import sys
for N in [1000,10000]:
    X,Y = [i for i in range(N)],(i for i in range(N))
    for x in [X,Y]:
        print(sys.getsizeof(x),end=' '*4)
    print() 
# 9024    88    
# 87624    88

#　这里同时可以看出使用()生成的迭代对象是几乎不占内存的
