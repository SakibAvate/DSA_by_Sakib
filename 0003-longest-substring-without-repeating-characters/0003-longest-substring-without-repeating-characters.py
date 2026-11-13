class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n= len(s)
        left = 0
        longest = 0
        my_dict={}
        for right in range(n):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]]+1)

            w = (right-left)+1
            longest = max(longest,w)
            my_dict[s[right]] = right

        return longest

