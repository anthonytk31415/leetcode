from collections import defaultdict

## build a hash table of all emails as keys and in the values, attach the owner of those emails 
## after each add, if the length of the hash table values > 1, then put it in a queue to 
## union find the parents 
## then union find the parents at the end 

def accountsMerge(accounts):

    def find(u, parent):
        if parent[u] != u: 
            return find(parent[u], parent)
        else: 
            return parent[u]

    def union(pU, pV, parent, rank):
        if rank[pU] >= rank[pV]:
            parent[pV] = pU
            rank[pU] += rank[pV]
        else: 
            parent[pU] = pV
            rank[pV] += rank[pU]
            
    parent = [i for i in range(len(accounts))]
    rank = [len(accounts[i]) - 1 for i in range(len(accounts))]

    emailTracker = defaultdict(list)
    for i, acct in enumerate(accounts):
        for j in range(1, len(acct)):
            curEmail = acct[j]
            emailTracker[curEmail].append(i)

    for email in emailTracker: 
        unions = emailTracker[email]
        if len(unions) > 1: 
            uIdx = unions[0]
            p_u = find(uIdx, parent)
            for vIdx in unions[1:]:
                p_v = find(vIdx, parent)
                if  p_u != p_v: 
                    union(p_u, p_v, parent, rank)

    for i in range(len(parent)):
        parent[i] = find(parent[i], parent)

    res = []
    for i, acct in enumerate(accounts):
        if parent[i] != i: 
            for x in accounts[i][1:]:
                accounts[parent[i]].append(x)

    for i, parent_i in enumerate(parent):
        if i == parent_i:
            emails = list(set(accounts[i][1:]))
            emails.sort()
            res.append(accounts[i][0:1] + emails) 
    return res


accounts = [["Lily","Lily3@m.co","Lily4@m.co","Lily17@m.co"],
            ["Lily","Lily5@m.co","Lily3@m.co","Lily23@m.co"],
            ["Lily","Lily0@m.co","Lily1@m.co","Lily8@m.co"],
            ["Lily","Lily14@m.co","Lily23@m.co"],
            ["Lily","Lily4@m.co","Lily5@m.co","Lily20@m.co"],
            ["Lily","Lily1@m.co","Lily2@m.co","Lily11@m.co"],
            ["Lily","Lily2@m.co","Lily0@m.co","Lily14@m.co"]]


# accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
print(accountsMerge(accounts))