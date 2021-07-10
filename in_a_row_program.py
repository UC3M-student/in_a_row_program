from numpy import random
response1 = input(" Tell us the lowest number\n")
response2 = input("Tell us the highest number. Add + 1\n")
user = input("How many times you want in a row. Add - 1\n")
choose = input("You´re chosen number is:\n")
choose1 = int(choose)
user1 = int(user)
response11 = int(response1)
response22 = int(response2)
answer1 = "Thanks, Be patient"
print(answer1)
userlist = list(range(response11,response22))
print(userlist)
p = 0
t = 0
n = 0
while p <= user1:
    p = 0
    t = t + 1
    while choose1 == int(random.choice((userlist))):
        p = p + 1
        n = n + 1
        #print(p)






porcent = (1/(n + t - user1)) * 100
print("El porcentaje de aparición es ",porcent)
print("Numero de veces ejecutado el programa:", n + t - user1)
