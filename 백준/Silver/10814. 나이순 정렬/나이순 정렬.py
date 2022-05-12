T = int(input())
signup_list = list()
for _ in range(T):
    age, name = input().split()
    signup_list.append((int(age), name))
sorted_signup_list = sorted(signup_list, key=lambda x: x[0])
for age, name in sorted_signup_list:
    print(f'{age} {name}')