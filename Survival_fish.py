a = input("Enter with space: ").split()
fish_size = list(map(int, a))
c = input("Enter with space: ").split()
flow_direction = list(map(int, c))
def solution(A, B):
    survived = 0       
    stack = []        

    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while len(stack)!= 0:
                if stack[-1] < A[i]:
                    stack.pop()
                else:
                    break
            else:
                survived += 1
    survived += len(stack)
    return survived
fish =  solution(fish_size,flow_direction)
print(f'The number of survived fish equals: {fish}')
