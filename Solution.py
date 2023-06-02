class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0
            current_sum = num1 + num2 + carry
            carry = current_sum // 2
            result = str(current_sum % 2) + result
            i -= 1
            j -= 1
        return result