#!/usr/bin/python3.5

import tracemalloc

NUM_OF_ATTR=10
NUM_OF_INSTANCE=100


'''
    optimize memory by python code
    refer to https://www.itcodemonkey.com/article/1347.html
'''


class Slots():
    __slots__=['attr%s'%i for i in range(NUM_OF_ATTR)]
    def __init__(self):
        value_lst=(1.0,True,[],{},())
        for i in range(NUM_OF_ATTR):
            setattr(self,'attr%s'%i,value_lst[i%len(value_lst)])

class NoSlots():
    def __init__(self):
        value_lst=(1.0,True,[],{},())
        for i in range(NUM_OF_ATTR):
            setattr(self,'attr%s'%i,value_lst[i%len(value_lst)])

def generate_some_objs():
    lst=[]
    for i in range(NUM_OF_INSTANCE):
        o = Slots() if i%2 else NoSlots()
        lst.append(o)
    return lst


if __name__ == '__main__':
    tracemalloc.start(3)
    t=generate_some_objs()

    snapshot=tracemalloc.take_snapshot()
    top_stats=snapshot.statistics('lineno')
    #top_stats=snapshot.statistics('filename')

    print(tracemalloc.get_traced_memory())
    for stat in top_stats[:10]:
        print(stat)

