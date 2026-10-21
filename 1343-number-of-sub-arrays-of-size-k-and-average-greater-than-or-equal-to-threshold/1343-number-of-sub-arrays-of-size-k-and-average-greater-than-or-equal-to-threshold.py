class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        win = sum(arr[:k])
        avg = 0
        count = 1 if (win/k) >= threshold else 0

        for i in range(k , len(arr)):
            win += arr[i] - arr[i - k]
            avg = win / k
            if avg >= threshold:
                count +=1
        
        return count