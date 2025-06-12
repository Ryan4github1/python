class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        val = [50, 40, 10, 5, 1]
        syms = ["L", "XL", "X", "V", "I"]
        num = self.number
        roman = ""
        for i in range(len(val)):
            count = num // val[i]
            roman += syms[i] * count
            num -= val[i] * count
        return roman

nums = [1, 5, 10, 15, 20, 30, 40, 50]
for a in nums:
    converter = RomanConverter(a)
    print(f"{a} = {converter.to_roman()}")