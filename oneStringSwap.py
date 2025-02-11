class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If the strings are already equal, no swap is needed
        if s1 == s2:
            return True

        # Find the positions where the characters differ
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]

        # To be almost equal, there should be exactly 2 differences, and they should be swappable
        return len(diff) == 2 and diff[0] == diff[1][::-1]

# Example usage
solution = Solution()
print(solution.areAlmostEqual("bank", "kanb"))  # Output: True
print(solution.areAlmostEqual("attack", "defend"))  # Output: False
print(solution.areAlmostEqual("abcd", "abdc"))  # Output: True
print(solution.areAlmostEqual("abcdefghijklmnop", "aaadefghijklmnop"))  # Output: False