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
                "Расчёт ИМТ и нормы воды для взрослых 18 – 65 лет."
                "Продолжить расчёт с этими формулами? (да/нет)",
            )
            confirm = input().strip().lower()
            if confirm != "да":
                print("Расчёт отменён. Обратитесь к врачу.")
                
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте ещё раз.")

# Ввод веса
while True:
    try:
        weight_kg = float(input("Введите свой вес (кг): "))
        if weight_kg < 30 or weight_kg >250:
            print(
                f"Ошибка: вес должен быть в диапазоне от 30 до 250 кг."
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
        if height_m < 0.5 or height_m > 2.5:
            print(
                f"Ошибка рост должен быть в диапиазоне от 0.5 до 2.5 м."
                f"Ds ddtkb {height_m} м. Попробуйте еще раз."
            )
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

if bmi is not None:
    print(f"Отчёт для пользователя: возраст, {num_1}")
    print(f"ИМТ: {bmi:.2f} | Категория: {category}")
    water_needed = water_requirement_assessment(weight_kg)
    print(f"Норма воды: {water_needed:.2f} л")
else:
    print("Не удалось рассчитать ИМТ из‑за некорректных данных.")

print("Расчёт окончен. Будьте здоровы!")
