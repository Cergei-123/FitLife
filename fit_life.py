print("Привет! Это фитнес трекер.")

# Сначала запрашиваем имя
num_0 = input("Введите, как вас зовут: ")

# Запрос сколько лет
while True:
    try:
        num_1 = int(input("Введите, сколько вам лет: "))
        if num_1 <= 0 or num_1 > 120:
            print("Пожалуйста, введите реалистичный возраст.")
            continue

        # Проверка на целевую группу для ИМТ/воды
        if not (18 <= num_1 <= 65):
            print(
                "Расчёт ИМТ и нормы воды по стандартным формулам предназначен для взрослых 18–65 лет. "
                "Для других возрастных групп рекомендации могут быть неточными. "
                "Продолжить расчёт с этими формулами? (да/нет)"
            )
            confirm = input().strip().lower()
            if confirm != "да":
                print("Расчёт отменён. Обратитесь к врачу для индивидуальных рекомендаций.")
                # Здесь можно выйти из программы или вернуть управление в другое место
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
        height_m = float(input("Введите свой рост в метрах: "))
        if height_m <= 0:
            print("Рост должен быть положительным числом. Попробуйте ещё раз.")
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте ещё раз.")

print()
print("Имя:", num_0)
print("Ваш возрасат:", num_1)
print("Вес:", weight_kg, "кг")
print("Рост:", height_m, "метров")


# Функция расчёта индекса массы тела
def body_mass_index(weight_kg, height_m):
    """
    Рассчитывает ИМТ и категорию по классификации ВОЗ.

    Возвращает кортеж (bmi_rounded, category) или (None, error_message).
    """
    if weight_kg <= 0 or height_m <= 0:
        return None, "Ошибка: вес и рост должны быть положительными числами."
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
bmi, category = body_mass_index(weight_kg, height_m)
if bmi is not None:

    print(f"Отчет для пользователя: {num_0}")
    print(f"\nТвой Индекс Массы Тела: {bmi}")
    print(f"Категория: {category}")

    water_needed = water_requirement_assessment(weight_kg)
    print(f"Рекомендуемая норма воды: {water_needed} л")
else:
    print("\nНе удалось рассчитать ИМТ из-за некорректных данных.")
    print(category)

print("Расчёт окончен. Будьте здоровы!")
