# Python script using loops
# for loop
for i in [1,2,3,4]:
    print(i)

for i in range(10):
    print("Cannot connect to the destination.")
    
# while loop
max_devices = 5
i = 1

while i < max_devices:
    print("User can still connect to additional devices")
    i = i + 1
    
print("User has reached maximum number of connected devices.")