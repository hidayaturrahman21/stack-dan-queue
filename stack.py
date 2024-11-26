stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print("Stack setelah push:", stack)

elemen = stack.pop()  
print("Elemen yang di-pop:", elemen)
print("Stack setelah di-pop:", stack)

if stack:
    print("Elemen teratas:", stack[-1])
else:
    print("Stack kosong")
