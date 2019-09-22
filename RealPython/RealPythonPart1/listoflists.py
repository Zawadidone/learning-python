universities = [
                        ['California	Institute	of	Technology',	2175,	37704],
                        ['Harvard',	19627,	39849],
                        ['Massachusetts	Institute	of	Technology',	10566,	40732],
                        ['Princeton',	7802,	37000],
                        ['Rice',	5879,	35551],
                        ['Stanford',	19535,	40569],
                        ['Yale',	11701,	40500]
]


def enrollment_stats(lists):
    fees = []
    students = []

    for l in lists:
        students.append(l[1])
        fees.append(l[2])

    return students, fees

totals = enrollment_stats(universities)


print(f"Total students: {sum(totals[0])}")
print(f"Total tuition:  {sum(totals[1])}")
