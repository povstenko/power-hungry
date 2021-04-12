from functools import reduce

def solution(xs):
    xs.sort()
    neg = [i for i in xs if i < 0]
    pos = [i for i in xs if i >=0]
    print(neg)
    print(pos)
    
    res = 1
    if len(neg) > 2:
        print(neg[:2])
        print(max(pos))
        res = reduce((lambda x, y: x*y), neg[:2]) * max(pos)
    else :
        print(pos[-3:])
        res = reduce((lambda x, y: x*y), pos[-3:])
    
    return res

# print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))