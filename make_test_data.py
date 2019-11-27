import random
test_size = 10
num_size = 10*test_size
with open(f"test_{test_size}.txt","w",encoding="utf-8") as file:
    for i in range(test_size):
        file.write(f"{random.randint(0,num_size)}\n")
