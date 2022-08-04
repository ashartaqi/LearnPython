class Train:

    def hello(self):
        print("hello boy")

    def gear(self):
        print("gather it")


class What(Train):

    def hello(self):
        print("never mind")


a = Train()
b = What()
a.gear()