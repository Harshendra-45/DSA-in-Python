class Solution(object):
    def processStr(self, s, k):
        length = 0

        # Calculate final length
        for ch in s:
            if ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
            else:
                length += 1

        if k >= length:
            return "."

        # Traverse backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch == '#':
                length //= 2
                k %= length

            elif ch == '%':
                k = length - 1 - k

            elif ch == '*':
                length += 1

            else:
                if k == length - 1:
                    return ch
                length -= 1

        return "."