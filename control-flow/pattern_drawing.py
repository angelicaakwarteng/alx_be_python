#Utilizing while loops and nested for loops to draw a simple text-based pattern.
number = int(input("Enter the size of the pattern: "))
rows = 0

while rows < number:
    for num in range(number):
        print("*", end="")
    print()
    rows+=1