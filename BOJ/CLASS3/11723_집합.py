import sys


def set_oper(oper):
    global se
    if oper == 'all':
        se.add({i for i in range(1, 21)})
    elif oper == 'empty':
        se.difference({i for i in range(1, 21)})
    else:
        oper, num = oper.split()
        if oper == 'add':
            se.add(num)
        elif oper == 'remove':
            se.difference({num})
        elif oper == 'check':
            if num in se:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if num in se:
                se.difference({num})
            else:
                se.add(num)
    return


M = int(input())
se = set()
for _ in range(M):
    oper = sys.stdin.readline()
    if oper == 'all':
        se.union({i for i in range(1, 21)})
    elif oper == 'empty':
        se = set()
    else:
        oper, num = oper.split()
        if oper == 'add':
            se.add(num)
        elif oper == 'remove':
            se.discard(num)
        elif oper == 'check':
            if num in se:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if num in se:
                se.discard(num)
            else:
                se.add(num)