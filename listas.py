alumno = ["Fulanito", "Vazquez", 15, "sagitario", 1.80, True]

print(f'El alumno {alumno[0]} {alumno[1]}, tiene {alumno[2]} años y es signo {alumno[3]}')
print(alumno)

del alumno[3]

alumno.append("Capricornio")
print(alumno)
