
studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    student_cijfer = []
    for cijfers in studentencijfers:
        student_cijfer.append(round(sum(cijfers) / len(cijfers), 2))
    return student_cijfer


def gemiddelde_van_alle_studenten(studentencijfers):
    student_cijfers = []
    for cijfers in studentencijfers:
        for i in cijfers:
            student_cijfers.append(i)
    return int(sum(student_cijfers) / len(student_cijfers))


print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
