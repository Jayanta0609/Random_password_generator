import random
passlen=int(input("Enter length of your password : "))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()?"
p="".join(random.sample(s,passlen))
print(p)