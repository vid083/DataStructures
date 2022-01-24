import collections
stack = collections.deque()
print(stack)        # output: deque([])

print(not stack)    # True

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)        # output: deque([10,20,30])

print(stack[-1])    # output: 30

stack.pop()
print(stack)        # output: deque([10,20])

stack.pop()
print(stack)        # output: deque([10])

stack.pop()
print(stack)        # output: deque([])

stack.pop()
print(stack)        # IndexError: pop from an empty deque