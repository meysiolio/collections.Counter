from collections import Counter

numShoes = int(input('please enter the number of shoes: '))

shoes_list = Counter(map(int,input().split()))

numCust = int(input())

income = 0
for i in range(numCust):
    shoe_size, price = map(int, input().split())
    if shoes_list[shoe_size] != 0:
        income +=  price
        shoes_list[shoe_size] -= 1

print(income)