def generate_arithmetic_progression(a, d, n):


a = 0
for i in range(1, 10):
    a = int(input('print'))
    return [a + d * i for i in range(n)]


progression = generate_arithmetic_progression(a, d, n)
print(progression)
