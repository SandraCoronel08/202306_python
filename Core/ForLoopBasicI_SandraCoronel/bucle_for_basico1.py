# Básicos
for num in range(151):
    print(num)
    
# Múltiplos de 5
for num in range(5, 1001, 5):
    print(num)

# Contando al estilo Dojo
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

# Whoa es un gran idiota
sum_odd = 0
for num in range(1, 500001, 2):
    sum_odd += num
print(sum_odd)

# Cuenta regresiva de a 4
for num in range(2018, 0, -4):
    print(num)

# Contador flexible
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)
