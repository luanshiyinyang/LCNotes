class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2id, email2name = {}, {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email2id:
                    email2name[email] = name
                    email2id[email] = len(email2id)
        
        uf = UnionFind(len(email2id))
        for account in accounts:
            first_index = email2id[account[1]]
            for other_email in account[2:]:
                uf.union(first_index, email2id[other_email])
        
        index2emails = collections.defaultdict(list)
        for email, index in email2id.items():
            index = uf.find(index)
            index2emails[index].append(email)
        
        res = []
        for emails in index2emails.values():
            res.append([email2name[emails[0]]] + sorted(emails))
        return res