class RomanNumerals:
    def __init__(self):
        self.table_from_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.table_to_roman = {1: "I", 4: "VI", 5: "V", 9: "XI", 10: "X", 40: "LX", 50: "L", 90: "CX",
                               100: "C", 400: "DC", 500: "D", 900: "MC", 1000: "M"}

    def from_roman(self, number: str) -> int:
        res = 0
        i = 0
        while i < len(number):
            if number[i] in ["VXLCDM"] and i != 0:
                if number[i - 1] in ["IXC"]:
                    res += self.table_from_roman[number[i]] - self.table_from_roman[number[i - 1]]
                    i += 2
            else:
                res += self.table_from_roman[number[i]]
                i += 1
        return res

    def to_roman(self, number: int) -> str:
        res = ""
        discharge = 0
        module = 1
        while number > 0:
            temp = number % 10 ** module
            if temp == 0:
                module += 1
                continue
            number -= temp
            while 5 * 10 ** discharge < temp < 9 * 10 ** discharge:
                res += self.table_to_roman[10 ** discharge]
                temp -= 1 + 10 ** discharge
            while 1 * 10 ** discharge < temp < 4 * 10 ** discharge:
                res += self.table_to_roman[10 ** discharge]
                temp -= 1 * 10 ** discharge
            res += self.table_to_roman[temp]
            discharge += 1
            module += 1
        return res[::-1]


print(RomanNumerals().from_roman(number="XXI"))
print(RomanNumerals().to_roman(number=1990))
