def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def is_good(permutation, R):
	for i in range(len(permutation)-1):
		if permutation[i] > permutation[i+1] and R[i] == '<':
			return False
		if permutation[i] < permutation[i+1] and R[i] == '>':
			return False
	return True


N = int(input())
R = input()

initial = list(range(1, N+1))
count = 1 if is_good(initial, R) else 0
p = initial[:]
next_permutation(p)
while p != initial:
	if is_good(p, R):
		count += 1
	next_permutation(p)
 
print(count)
