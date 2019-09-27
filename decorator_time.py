import time

def timer_wrapper(func):
    def func_wrapper(param):
        NUM_RUNS = 100000
        avg_time = 0
        for i in range(NUM_RUNS):
            t0 = time.time()
            func(param)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= NUM_RUNS
        print("Выполнение заняло в среднем %.8f секунд" % avg_time)
        return func(param)
    return func_wrapper
def fibanachi(elem_1, elem_2):
    return elem_1+elem_2

class timer_dec:
    def __init__(self, function):
        self.NUM_RUNS=100000
        self.function=function

    def __call__(self, *args, **kwargs):
        avg_time = 0
        for i in range(self.NUM_RUNS):
            t0 = time.time()
            self.function(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.NUM_RUNS
        print("Выполнение заняло в среднем %.8f секунд" % avg_time)
        return self.function(*args,**kwargs)


@timer_wrapper
def fibl(num):
    fibanachi_list=[1,2]
    for i in range(num-2):
        elem_3=fibanachi(fibanachi_list[-1], fibanachi_list[-2])
        if elem_3 > 4000000: break
        fibanachi_list.append(elem_3)
    return fibanachi_list

@timer_dec
def fibl_2(num):
    fibanachi_list=[1,2]
    for i in range(num-2):
        elem_3=fibanachi(fibanachi_list[-1], fibanachi_list[-2])
        if elem_3 > 4000000: break
        fibanachi_list.append(elem_3)
    return fibanachi_list

fibl(4000)

fibl_2(4000)




