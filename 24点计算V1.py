# encoding=utf-8
import itertools
import random as rd

def get_24point(nums,target):
    iis = list(itertools.permutations(nums,4))
    for ii in iis:
        indexs = set(range(len(ii)))
        for index in list(itertools.combinations(indexs,2)):
            left_index = tuple(indexs - set(index))
            num1 = ii[index[0]]
            num2 = ii[index[1]]
            num3 = ii[left_index[0]]
            num4 = ii[left_index[1]]
            for operate1 in ['+','-','*','/']:
                try:
                    num11 = eval('{}{}{}'.format(num1,operate1,num2))
                except:
                    pass
                for operate2 in ['+','-','*','/']:
                    try:
                        num22 = eval('{}{}{}'.format(num3,operate2,num4))
                    except:
                        pass
                    for operate3 in ['+','-','*','/']:
                        try:
                            result = eval('{}{}{}'.format(num11,operate3,num22))
                        except:
                            pass
                        if result == target:
                            print('({}{}{}){}({}{}{})={}'.format(num1,operate1,num2,operate3,num3,operate2,num4,target))
                        else:
                            pass
if __name__ == '__main__':
    get_24point(nums = [rd.randint(1,10) for i in range(4)],target=24)
