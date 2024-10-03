n = int(input())
arr = map(int, input().split())

check = set(arr)

result = sorted(check,reverse=True)

print(result)
print(result[1])