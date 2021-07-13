class romanToInt:
    def romanToInt(self, s: str) -> int:
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        previous = 0
        result = 0
        for x in s[::-1]:
            current = romanMap[x]
            if previous > current:
                result -= current
            else:
                result += current
            previous = current
        return result
            
