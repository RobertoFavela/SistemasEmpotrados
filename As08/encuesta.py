total_students = 0
total_age_male = 0
total_age_female = 0
count_male = 0
count_female = 0
count_foreign_male = 0
count_foreign_female = 0
count_assistance_house = 0
count_female_share_house = 0
count_male_live_alone = 0

while True:
    try:
        age = int(input("Edad: "))
        if age == 0:
            break
        if age < 0:
            print("Edad no inválida.")
            continue
        
        sex = input("Sexo (M/F): ").strip().upper()
        if sex not in ('M', 'F'):
            print("Sexo inválido.")
            continue
        
        origin = input("Procedencia (L/F): ").strip().upper()
        if origin not in ('L', 'F'):
            print("Procedencia inválida.")
            continue
        
        total_students += 1

        if sex == 'M':
            total_age_male += age
            count_male += 1
        else:
            total_age_female += age
            count_female += 1

        if origin == 'F':
            if sex == 'M':
                count_foreign_male += 1
            else:
                count_foreign_female += 1

            desired_housing = input("Vivienda deseada (A/C/S): ").strip().upper()
            if desired_housing not in ('A', 'C', 'S'):
                print("Opción de vivienda inválida.")
                continue
            
            if desired_housing == 'A':
                count_assistance_house += 1
            elif desired_housing == 'C' and sex == 'F':
                count_female_share_house += 1
            elif desired_housing == 'S' and sex == 'M':
                count_male_live_alone += 1
    
    except ValueError:
        print("Entrada inválid.")

if total_students > 0:
    avg_age_male = total_age_male / count_male if count_male > 0 else 0
    avg_age_female = total_age_female / count_female if count_female > 0 else 0
    percent_foreign_male = (count_foreign_male / total_students) * 100
    percent_foreign_female = (count_foreign_female / total_students) * 100
    percent_assistance_house = (count_assistance_house / total_students) * 100
    percent_female_share_house = (count_female_share_house / total_students) * 100
    percent_male_live_alone = (count_male_live_alone / total_students) * 100

    print(f"\nTotal de alumnos encuestados: {total_students}")
    print(f"Edad promedio de los alumnos hombres: {avg_age_male:.2f}")
    print(f"Edad promedio de las alumnas mujeres: {avg_age_female:.2f}")
    print(f"Porcentaje de alumnos hombres foráneos: {percent_foreign_male:.2f}%")
    print(f"Porcentaje de alumnas mujeres foráneas: {percent_foreign_female:.2f}%")
    print(f"Porcentaje de alumnos que desean vivir en casa de asistencia: {percent_assistance_house:.2f}%")
    print(f"Porcentaje de alumnas mujeres que desean compartir casa: {percent_female_share_house:.2f}%")
    print(f"Porcentaje de alumnos hombres que desean vivir solos: {percent_male_live_alone:.2f}%")
else:
    print("No se ingresaron datos.")

