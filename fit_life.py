print("Привет! Это фитнес трекер.")

# Сначала запрашиваем имя
num_0 = input("Введите, как вас зовут: ")

# Ввод дня рождения
while True:
    try:
        num_1 = int(input("Введите день рождения: "))
        if not (1 <= num_1 <= 31):
            print("День должен быть от 1 до 31. Попробуйте ещё раз.")
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте ещё раз.")

# Ввод месяца рождения
while True:
    try:
        num_2 = int(input("Введите месяц рождения: "))
        if not (1 <= num_2 <= 12):
            print("Месяц должен быть от 1 до 12. Попробуйте ещё раз.")
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте ещё раз.")

# Ввод веса
while True:
    try:
        weight_kg = float(input("Введите свой вес (кг): "))
        if weight_kg <= 0:
            print("Вес должен быть положительным числом. Попробуйте ещё раз.")
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте ещё раз.")

# Ввод роста
while True:
    try:
        height_cm = float(input("Введите свой рост (см): "))
        if height_cm <= 0:
            print("Рост должен быть положительным числом. Попробуйте ещё раз.")
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте ещё раз.")

print()
print("Имя:", num_0)
print("День рождения:", num_1)
print("Месяц рождения:", num_2)
print("Вес:", weight_kg, "кг")
print("Рост:", height_cm, "см")


# Функция расчёта индекса массы тела
def body_mass_index(weight_kg, height_cm):
    """
    Рассчитывает ИМТ и категорию по классификации ВОЗ.

    Возвращает кортеж (bmi_rounded, category) или (None, error_message).
    """
    if weight_kg <= 0 or height_cm <= 0:
        return None, "Ошибка: вес и рост должны быть положительными числами."
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    bmi_rounded = round(bmi, 2)

    if bmi < 18.5:
        category = "Недостаточная масса тела."
    elif 18.5 <= bmi < 24.9:
        category = "Нормальная масса тела."
    elif 25.0 <= bmi < 29.9:
        category = "Избыточная масса тела (предожирение)."
    else:
        category = "Ожирение."
    return bmi_rounded, category


# расчет потребления воды
def water_requirement_assessment(weight_kg):
    """
    Рассчитывает норму потребления воды.

    Рассчитывает обьем в литрах.
    """
    water_ml = weight_kg * 30
    return water_ml / 1000


# Расчёт ИМТ
bmi, category = body_mass_index(weight_kg, height_cm)
if bmi is not None:



    print("Ваш ИМТ:", bmi)
    print("Категория:", category)
    water_needed = water_requirement_assessment(weight_kg)
    print("Рекомендуемая норма воды:", water_needed, "л")
else:
    print("Не удалось рассчитать ИМТ из-за некорректных данных.")
    print(category)

print("Расчет окончен. Будьте здоровы!")
