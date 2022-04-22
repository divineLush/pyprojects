class Calc:
    def __init__(self, value = None):
        self.value = value


    def show(self):
        print(self.value)


    def __str__(self):
        return str(self.value)


    def _check_num(self, num):
        is_int = type(num) == int
        is_float = type(num) == float

        return is_int or is_float


    def sum(self, num):
        if (self.value is None):
            self.value = num
            return

        if (self._check_num(num)):
            self.value += num


    def subtr(self, num):
        if (self.value is None):
            self.value = num
            return

        if (self._check_num(num)):
            self.value -= num


    def mult(self, num):
        if (self.value is None):
            self.value = num
            return

        if (self._check_num(num)):
            self.value *= num


    def div(self, num):
        if (self.value is None):
            self.value = num
            return

        if (self._check_num(num)):
            self.value /= num



C = Calc()
C.show()
C.sum(2)
C.show()
C.subtr(3)
C.show()
C.subtr("123")
C.show()
C.mult(5)
C.show()
print(C.__str__())
