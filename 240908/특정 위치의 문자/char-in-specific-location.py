arr = [ 'L', 'E', 'B', 'R', 'O', 'S']

word = input()

if word in arr:
    position = arr.index(word)
    print(position)
else:
    print("None")