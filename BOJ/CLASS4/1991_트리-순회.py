import collections


def post(n):
    global post_str
    if c1_dict[n] != 0:
        post(c1_dict[n])
    if c2_dict[n] != 0:
        post(c2_dict[n])
    post_str += n


def pre(n):
    global pre_str
    pre_str += n
    if c1_dict[n] != 0:
        pre(c1_dict[n])
    if c2_dict[n] != 0:
        pre(c2_dict[n])


def mid(n):
    global mid_str
    if c1_dict[n] != 0:
        mid(c1_dict[n])
    mid_str += n
    if c2_dict[n] != 0:
        mid(c2_dict[n])

N = int(input())
parent_dict = collections.defaultdict(int)
c1_dict = collections.defaultdict(int)
c2_dict = collections.defaultdict(int)

for _ in range(N):
    p, c1, c2 = input().split()
    if c1 != '.':
        c1_dict[p] = c1
    if c2 != '.':
        c2_dict[p] = c2
    parent_dict[c1] = p
    parent_dict[c2] = p

post_str = ''
pre_str = ''
mid_str = ''

post('A')
pre('A')
mid('A')
print(pre_str)
print(mid_str)
print(post_str)