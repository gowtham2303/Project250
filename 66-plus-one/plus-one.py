class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=""
        for i in range(len(digits)):
            x+=str(digits[i])
        y=int(x)
        digits.clear()
        y+=1
        x=str(y)
        for i in x:
            digits.append(int(i))
        return digits