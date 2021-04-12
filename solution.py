from functools import reduce

def solution(xs):
    if len(xs) == 0:
        return str(0)
    elif len(xs) == 1:
        return str(xs[0])

    pos = [i for i in xs if i > 0]
    neg = [i for i in xs if i < 0]

    if len(neg) % 2 == 1:
        neg.remove(max(neg))

    if len(neg) == 0 and len(pos) == 0:
        return str(0)

    res = reduce((lambda x,y: x*y), pos + neg)
    
    return str(res)

# print(solution([2, 0, 2, 2, 0]))
# print(solution([-2, -3, 4, -5]))
