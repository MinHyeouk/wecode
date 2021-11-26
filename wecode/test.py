def get_even():
    a = []
    for i in range(1, 50):
        if i % 2 == 0:
            a.append(i)
    return a

print(get_even())