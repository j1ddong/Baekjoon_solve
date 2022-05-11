from collections import defaultdict


g, s = map(int, input().split())
W = input()
S = input()
cnt = 0

W_dict = defaultdict(int)
S_dict = defaultdict(int)
for i in range(g):
    W_dict[W[i]] += 1
    S_dict[S[i]] += 1
if W_dict == S_dict:
    cnt += 1

for j in range(g, s):
    S_dict[S[j]] += 1
    S_dict[S[j - g]] -= 1
    if S_dict[S[j - g]] == 0:
        del S_dict[S[j - g]]
    if W_dict == S_dict:
        cnt += 1
print(cnt)
