def make_adder(n):
    def adder(k):
        return k + n
    return adder
print(make_adder(5))