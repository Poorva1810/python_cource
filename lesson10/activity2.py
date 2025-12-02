class computer:
    def __init__(self):
        self.__maxprise=900
    def sell(self):
        print("selling prise: {}".format(self.__maxprise))
    def setmaxprise(self,prise):
        self.__maxprise=prise
c=computer()
c.sell()
c.__maxprise=1000
c.sell() 
c.setmaxprise(1000)
c.sell()               