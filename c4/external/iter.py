class PowNumber:
    """
    生成1,2,3,4,5等数的平方
    """

    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 5:
            raise StopIteration
        return self.value * self.value

    def __iter__(self):
        return self

if __name__ == '__main__':
    pow = PowNumber()

    print(pow.__next__())
    print(pow.__next__())
    print(pow.__next__())
    print(pow.__next__())
    print(pow.__next__())

    #print(next(pow))
    #print(next(pow))
    #print(next(pow))
    #print(next(pow))
    #print(next(pow))
    #print(next(pow))
    '''
    for i in pow:
        print(i)
    print(next(pow))
    '''