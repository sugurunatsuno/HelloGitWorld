def check_worktimes(start, end):
    if start > end:
        return 24 - start + end
    elif start == end:
        return 1
    else:
        return end - start

print(check_worktimes(15, 23))
print(check_worktimes(9, 9))
print(check_worktimes(23, 1))
