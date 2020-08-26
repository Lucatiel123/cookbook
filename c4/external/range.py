# range
# 左闭右开

class genRange:

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def get_number(self):
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start

class iterRange:

    def __init__(self, start, end):
        self.start = start -1
        self.end =  end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self

def get_number(start, end):
    start -= 1
    while True:
        if start >= end:
            break
        start += 1
        yield start

if __name__ == '__main__':
    gen_num = genRange(5, 10)
    print(list(gen_num.get_number()))
    iter_num = iterRange(5, 10)
    for i in iter_num:
        print(i)
    num = get_number(5, 10)
    print(num)
    print(list(num))
