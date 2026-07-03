prices = [11500, 29000, 34000, 52000, 80000,110000]
user_price = int(input("Enter target price: "))
low = 0
high = len(prices) - 1
answer = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= user_price:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

if answer != -1:
    print("First product price =", prices[answer])
else:
    print("No product found")
