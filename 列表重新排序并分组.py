import math

# 将一个list中的元素进行重新排序并分组
# 首尾放到一组
def rerank_list(list_box):
    assert isinstance(list_box,list),'请输入一个list'
    box_len = len(list_box)
    new_list = []
    for i in range(math.ceil(box_len/2)):
        tmp = set([list_box[i],list_box[box_len-i-1]])
        new_list = new_list + list(tmp)
    return new_list
# 将重新排序的数据进行分组
def list2group(list_box,numbers):
    '''
    list_box:输入的列表，已进行排序
    numbers:每组多少个元素
    '''
    assert isinstance(list_box,list),'请输入一个列表'
    assert isinstance(numbers,int),'请输入一个整数'
    for i in range(0,len(list_box),numbers):
        yield list_box[i:i+numbers]
if __name__ == '__main__':
    list_box = [1, 2, 3, 4, 5, 6, 7]
    print(rerank_list(list_box))
    print(list(list2group(list_box,2)))
