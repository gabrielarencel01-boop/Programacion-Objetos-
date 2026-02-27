from ESCUELA import *

alumno1 = Alumno("Renata Rangel", 34214213)
alumno2 = Alumno("Marco Serrano", 39283)
alumno3 = Alumno("Alfredo Gaspar", 12314)
alumno4 = Alumno("Sughey Martinez", 28370)
alumno5 = Alumno("Zoe Titla", 96548)



alumno1.agregar_calificacion(95)
alumno1.agregar_calificacion(90)

alumno2.agregar_calificacion(95)
alumno2.agregar_calificacion(70)
alumno2.agregar_calificacion(98)

alumno3.agregar_calificacion(65)
alumno3.agregar_calificacion(72)
alumno3.agregar_calificacion(61)
alumno3.agregar_calificacion(65)

alumno4.agregar_calificacion(55)
alumno4.agregar_calificacion(60)
alumno4.agregar_calificacion(88)

alumno5.agregar_calificacion(75)
alumno5.agregar_calificacion(80)
alumno5.agregar_calificacion(68)

print(f"La alumna {alumno1.nombre} tiene promedio de: {alumno1.calcular_promedio():.2f} y esta: {alumno1.estado_final()}")
print(f"La alumna {alumno2.nombre} tiene promedio de: {alumno2.calcular_promedio():.2f} y esta: {alumno2.estado_final()}")
print(f"La alumna {alumno3.nombre} tiene promedio de: {alumno3.calcular_promedio():.2f} y esta: {alumno3.estado_final()}")
print(f"La alumna {alumno4.nombre} tiene promedio de: {alumno1.calcular_promedio():.2f} y esta: {alumno4.estado_final()}")
print(f"La alumna {alumno5.nombre} tiene promedio de: {alumno2.calcular_promedio():.2f} y esta: {alumno5.estado_final()}")

grupo1=Grupo("Progra")
grupo1.agregar_alumno(alumno1)
grupo1.agregar_alumno(alumno2)
grupo1.agregar_alumno(alumno3)
grupo1.agregar_alumno(alumno4)
grupo1.agregar_alumno(alumno5)
print(grupo1.mostrar_promedios())
print(grupo1.mejor_alumno())

