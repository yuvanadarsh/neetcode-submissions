class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for item in strs:
            key = "".join(sorted(item))
            m[key].append(item)
        return list(m.values())