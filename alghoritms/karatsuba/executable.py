from funcs import karatsuba, recursive_karatsuba


x = 1685287499328328297814655639278583667919355849391453456921116729
y = 7114192848577754587969744626558571536728983167954552999895348492
counter_1 = 0
counter_2 = 0
counter_3 = 0

print(recursive_karatsuba(x, y))
print(x*y)
print(counter_1, counter_2, counter_3)
