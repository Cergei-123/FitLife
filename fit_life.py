print("Привет! Это фитнес трекер.")

# Сначала запрашиваем имя
num_0 = input("Введите, как вас зовут: ")

# Запрос сколько лет
while True:
    num_1 = input("Введите, сколько вам лет: ")
    if num_1.isdigit() and 0 < int(num_1) <= 120:
        num_1 = int(num_1)
        break
    print("Пожалуйста, введите реалистичный возраст (от 1 до 120).")

# Проверка на целевую группу для ИМТ/воды

    if not (18 <= num_1 <= 65):
        print("Расчёт ИМТ и нормы воды для взрослых 18 – 65 лет.")
        confirm = input().strip().lower()
        if confirm != "да":
            print("Расчёт отменён. Обратитесь к врачу.")
            exit()

    break
print("Ошибка: нужно ввести целое число. Попробуйте ещё раз.")

# Ввод веса
while True:
    try:
        weight_kg = float(input("Введите свой вес (кг): "))
        if weight_kg < 30 or weight_kg > 120:
            print(
                f"Ошибка: вес должен быть в диапазоне от 30 до 120 кг."
                f"Вы ввели: {weight_kg} кг. Попробуйте ещё раз.",
            )
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте ещё раз")

# Ввод роста
while True:
    try:
        height_m = float(input("Введите свой рост в метрах: "))
        if height_m < 0.5 or height_m > 2:
            print(
                f"Ошибка рост должен быть в диапиазоне от 0.5 до 2 м."
                f"{height_m} м. Попробуйте еще раз.",
            )
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте ещё раз.")

print()
print("Имя:", num_0)
print("Ваш возраст:", num_1)
print("Вес:", weight_kg, "кг")
print("Рост:", height_m, "метров")


# Функция расчёта индекса массы тела
def body_mass_index(weight_kg, height_m):

    """
    Рассчитывает ИМТ и категорию по классификации ВОЗ.

    Возвращает кортеж (bmi_rounded, category) или (None, error_message).
    """

    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Недостаточная масса тела."
    elif 18.5 <= bmi < 24.9:
        category = "Нормальная масса тела."
    elif 25.0 <= bmi < 29.9:
        category = "Избыточная масса тела (предожирение)."
    else:
        category = "Ожирение."
    return bmi, category


# расчет потребления воды
WATER_ML_PER_KG = 30


def water_requirement_assessment(weight_kg):
    """
    Рассчитывает норму потребления воды.

    Рассчитывает обьем в литрах.
    """
    water_ml = weight_kg * WATER_ML_PER_KG
    return water_ml / 1000


# Расчёт ИМТ
bmi, category = body_mass_index(weight_kg, height_m)
water_needed = water_requirement_assessment(weight_kg)
print(f"Отчет для пользователя: {num_0}")
print(f"Возраст, {num_1}")
print(f"ИМТ: {bmi:.2f} | Категория: {category}")
print(f"Норма воды: {water_needed:.2f} л")
print("Расчёт окончен. Будьте здоровы!")
