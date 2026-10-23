s = input()

seen = set()
left = 0
max_length = 0

for right in range(len(s)):
    if s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    length = right - left + 1
    if max_length < length:
        max_length = length

print(max_length)