class Stack:
    def __init__(ran):
        ran.items = []
    def is_empty(ran):
        return ran.items==[]
    def push(ran,data):
        ran.items.append(data)
    def pop(ran):
        return ran.items.pop()
s=Stack()
t=input()
for character in t:
    s.push(character)
reversed_text=''
while not s.is_empty():
    reversed_text=reversed_text+s.pop()
if t==reversed_text:
    print('YES')
else:
    print('NO')
