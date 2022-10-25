class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self, other):
        return 'The value is' + str(other.value)


number = Number(20)
number.__str__()