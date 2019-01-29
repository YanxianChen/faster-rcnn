import time


class Timer(object):
    '''一个简单的计时器：一个有五个属性：所有线程调用的总时间，所有线程总调用次数，
    单个线程开始时间，单个线程的使用时间，所有线程总调用平均时间'''

    def __init__(self):
        self.total_time = 0.
        self.calls = 0
        self.start_time = 0.
        self.diff = 0.
        self.average_time = 0.

    # 进程开始时调用
    def tic(self):
        self.start_time = time.time()

    # 进程结束时调用
    def toc(self, average=True):
        self.diff = time.time() - self.start_time
        self.total_time += self.diff
        self.calls += 1
        self.average_time = self.total_time / self.calls

        if average:
            return self.average_time
        else:
            return self.diff
