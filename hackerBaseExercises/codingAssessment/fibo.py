def solution(n):
    frst_nbr = 0
    scnd_nbr = 1
    if n == 0:
        return (frst_nbr)
    elif n == 1:
        return (frst_nbr)
    else:
        for i in range(2, n + 1):
            result = frst_nbr + scnd_nbr
            frst_nbr = scnd_nbr
            scnd_nbr = result
        return scnd_nbr
    
print(solution(0))  # Output: 0
print(solution(1))  # Output: 0
print(solution(2))  # Output: 1
print(solution(3))  # Output: 2
print(solution(4))  # Output: 3
print(solution(5))  # Output: 5
print(solution(6))  # Output: 8