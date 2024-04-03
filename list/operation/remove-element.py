list_3 = [10, 70, 20, 70]

list_3.remove(70)
print(list_3)

list_3.remove(70)
print(list_3)

# method pop()
list_3 = [10, 70, 20, 70]

x = list_3.pop(2)
print('list_3:', list_3)
print('removed element:', x)

x = list_3.pop()
print('list_3:', list_3)
print('removed element:', x)