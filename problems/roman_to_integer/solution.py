class Solution:
    def romanToInt(self, s: str) -> int:
        a = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        answer = 0
        for i in range(len(s)):
            if i > 0 and a[s[i]] > a[s[i-1]]:
                answer += a[s[i]] - 2 * a[s[i-1]]
            else:
                answer += a[s[i]]
        return answer