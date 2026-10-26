print("Привет! Это фитнес-трекер.")

name = input("Введите, как вас зовут: ")

# Возраст
while True:
    age_input = input("Введите ваш возраст: ")
    if age_input.isdigit():
        age = int(age_input)
        if 0 < age <= 120:
            break
    print("Пожалуйста, введите реалистичный возраст (от 1 до 120).")

# Проверка целевой группы
if not (18 <= age <= 65):
    print("Расчёт ИМТ предназначен для взрослых 18–65 лет.")
    confirm = input("Вы всё равно хотите продолжить?").strip().lower()
    if confirm != "да":
        print("Расчёт отменён, обратитесь к врачу.")
        exit()

# Вес
while True:
    try:
        weight_kg = float(input("Введите свой вес (кг): "))
        if not (30 <= weight_kg <= 120):
            print(f"Ошибка: вес должен быть от 30 до 120 кг.")
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте ещё раз.")

# Рост
while True:
    try:
        height_m = float(input("Введите свой рост в метрах: "))
        if not (0.5 <= height_m <= 2):
            print(f"Ошибка: рост должен быть от 0.5 до 2 м.")
            continue
        break
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте ещё раз.")

print()
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Вес: {weight_kg} кг")
print(f"Рост: {height_m} метров")


# Функция: возвращает сразу bmi и категорию
def get_bmi_and_category(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        return bmi, "Недостаточная масса тела."
    if bmi < 25.0:
        return bmi, "Нормальная масса тела."
    if bmi < 30.0:
        return bmi, "Избыточная масса тела (предожирение)."
    return bmi, "Ожирение."


bmi, category = get_bmi_and_category(weight_kg, height_m)

# Вода
WATER_ML_PER_KG = 30
NUMBER = 1000
water_needed_liters = (weight_kg * WATER_ML_PER_KG) / NUMBER

print(f"\nОтчёт для пользователя: {name}")
print(f"ИМТ: {bmi:.2f} ({category})")          
print(f"Рекомендуемая норма воды: {water_needed_liters:.2f} л")
print("Расчёт завершён. Будьте здоровы!")
