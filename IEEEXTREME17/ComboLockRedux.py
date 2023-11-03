from collections import deque

mod = 10**9 + 9

def generate_allowable_sequence(h_0, a, b, q, n):
    sequence = [h_0]
    for i in range(1, 10**6):
        next_code = (sequence[-1] * a + b) % q
        if next_code == h_0:
            break
        sequence.append(next_code)
    return sequence

def change_possible(start, target, sequence, n):
    visited = set()
    visited.add(start)
    queue = deque([(start, 0)])
    min_changes = float('inf')
    ways_to_reach = {start: 1}
    while queue:
        current, changes = queue.popleft()
        if current == target:
            min_changes = min(min_changes, changes)
            continue
        for s in sequence:
            next_code = (current + s) % (10**n)
            if next_code not in visited:
                visited.add(next_code)
                queue.append((next_code, changes + 1))
            if next_code in ways_to_reach:
                ways_to_reach[next_code] = (ways_to_reach[next_code] + ways_to_reach[current]) % mod
            else:
                ways_to_reach[next_code] = ways_to_reach[current]
    return -1 if min_changes == float('inf') else min_changes, ways_to_reach[target]

# Input reading
c = int(input())
for _ in range(c):
    n, target, h_0, a, b, q = input().split()
    n = int(n)
    target = int(target)
    h_0 = int(h_0)
    a = int(a)
    b = int(b)
    q = int(q)

    sequence = generate_allowable_sequence(h_0, a, b, q, n)
    min_changes, ways_to_reach = change_possible(0, target, sequence, n)
    print(min_changes, ways_to_reach)
    
