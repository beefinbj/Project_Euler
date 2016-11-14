power = 1

for i in range(7830457):
    power = power*2
    if len(str(power)) > 10:
        power = int(str(power)[-10:])

power = power*28433
power = int(str(power)[-10:])
power += 1
print power
