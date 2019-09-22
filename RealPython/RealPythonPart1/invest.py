def invest(amount, rate, time): # calculate compound interest to track the growth of an investment
    print(f"principal amount: ${amount}")
    print(f"annual rate of return: {rate}")
    for i in range(1, time + 1):
        amount = amount * (1 + rate)
        print(f"year {i}: ${amount}")
    print()

invest(100,	.05,	8)
invest(2000, .025,	5)
