import queue
stack = queue.LifoQueue()
print(stack)        #output: <queue.LifoQueue object at 0x10113a7f0>

stack.put(10)
stack.put(20)
stack.put(30)
print(stack)

stack.get()
stack.get()

