li = ["가위", "바위", "보"]
result = ""
a = input()
b = input()
if a == li[0]:
   if b == li[0]:
      result = "Result : Draw"
   elif b == li[1]:
      result = "Result : Man2 Win!"
   elif b == li[2]:
      result = "Result : Man1 Win!"
elif a == li[1]:
   if b == li[0]:
      result = "Result : Man1 Win!"
   elif b == li[1]:
      result = "Result : Draw"
   elif b == li[2]:
      result = "Result : Man2 Win!"
elif a == li[2]:
   if b == li[0]:
      result = "Result : Man2 Win!"
   elif b == li[1]:
      result = "Result : Man1 Win!"
   elif b == li[2]:
      result = "Result : Draw"
print(result)