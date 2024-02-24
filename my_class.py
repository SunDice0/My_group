age = 0 
amount = 0
suma = 0
name =""
with open("my_group.txt","a",encoding="utf-8")as file:
    for line in file:
        line = line.split(" ")
        if age<int(line[2]):
            age = int(line[2])
            name = line[0]
        suma+=int(line[2])
        amount+=1

print("Найстарший учень:",name, "-",age)
print("Середній вік групи:", suma/amount)
