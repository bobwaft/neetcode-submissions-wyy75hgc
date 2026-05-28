class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        length = 0
        freq = Counter()
        for r in range(len(s)):
            freq[s[r]] += 1
            mostCommon = freq.most_common(1)[0]
            while r-l+1 - mostCommon[1] > k:
                freq[s[l]] -= 1
                l += 1
            length = max(length,r-l+1)
        return length