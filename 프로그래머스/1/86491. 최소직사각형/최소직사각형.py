def solution(sizes):
    longest = max(sizes[0])
    short_long = min(sizes[0])
    for size in sizes:
        longest = max(longest, max(size))
        short_long = max(short_long, min(size))
    return longest * short_long