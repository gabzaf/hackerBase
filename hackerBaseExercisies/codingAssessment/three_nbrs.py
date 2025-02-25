#Given three numbers a, b and n, calculate the nth number in the sequence where each number is the sum of the previous two numbers, starting with
#a and b. Return the nth number in the sequence, as well as the sum of the first n numbers and the average of the first n numbers. Example -
#For an input of: 2, 5, 6 expects an object output of:{"nth": 31, "sum": 76, "average": 12.666666666666}

def solution(a, b, n):
    if n == 1:
        return {"nth": a, "sum": a, "average": a}
    elif n == 2:
        return {"nth": b, "sum": a + b, "average": (a + b) / 2}
    
    sequence = [a, b]
    
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)
    
    nth_number = sequence[-1]
    sum_of_sequence = sum(sequence)
    average_of_sequence = sum_of_sequence / n 
    
    return {"nth": nth_number, "sum": sum_of_sequence, "average": average_of_sequence}


a = 2
b = 5
n = 6
result = solution(a, b, n)
print(result)