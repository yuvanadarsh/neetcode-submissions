class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        visited = defaultdict(list)

        for item in strs:
            temp = "".join(sorted(item))
            if(temp in visited):
                visited[temp].append(item)
            else:
                visited[temp] = [item]

        for key in visited:
            res.append(visited[key])

        return res