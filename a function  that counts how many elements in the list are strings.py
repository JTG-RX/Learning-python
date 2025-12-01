def count_str(n):
    count = 0
    for i in n:
        if type(i) == str:
            count += 1
    return count

print(count_str(null))
