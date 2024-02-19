class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5,'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # mult_5 = {'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M'}
        idx = len(s) - 1
        val = 0
        # power = 1
        while idx >= 0:
            if idx == 0:
                val += map[s[idx]]
                break
            if map[s[idx - 1]] < map[s[idx]]: # sub
                val += map[s[idx]] - map[s[idx - 1]]
                idx -= 2
            else:
                val += map[s[idx]]
                idx -= 1
        return val


print(Solution().romanToInt("LVIII"))