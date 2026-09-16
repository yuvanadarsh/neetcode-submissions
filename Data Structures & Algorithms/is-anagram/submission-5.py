class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counts = defaultdict(int)

        for item in s:
            letter_counts[item] += 1

        for item in t:
            if letter_counts[item] == 0:
                return False
            letter_counts[item] -= 1

        return all(value == 0 for value in letter_counts.values())