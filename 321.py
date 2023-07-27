str = input()
result_a = 0
result_b = 0

for i in range(int(len(str)/2)):
    result_a+=int(str[i])
    
for i in range(int(len(str)/2),len(str)):
    result_b+=int(str[i])

if (result_a == result_b):
    print("LUCKY")
else:
    print("READY")
