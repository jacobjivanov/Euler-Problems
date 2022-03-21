base = 2
exponent = 1000
power = base ** exponent

power = list(str(power))
print("2 to the 1000th power: " + str(power))

power_digit_sum = 0
for digit in power:
	power_digit_sum += int(digit)

print("Sum of digits: " + str(power_digit_sum))

# Answer: 1366