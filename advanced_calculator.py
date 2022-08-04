class Calculator:

    @staticmethod
    def greet():
        print("hello")

    def __init__(self, number):
        self.number = number

    def square(self):
        return f'the square of this number is {self.number * self.number}'

    def cube(self):
        return f"the cube of this number is {self.number * self.number * self.number}"

    def square_root(self):
        return f"the square root of this number is {self.number **0.5}"


num = input(Calculator())
