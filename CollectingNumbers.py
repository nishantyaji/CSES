n = int(input().strip())
x = list(map(int, input().strip().split()))
my_dict = {y: i + 1 for i, y in enumerate(x)}
num_rounds = 0
for i in x:
    if i != n and my_dict[i] > my_dict[i+1]:
        num_rounds += 1
print(num_rounds + 1)