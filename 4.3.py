import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import random

fake = Faker('ru_Ru')

years = [2021, 2022, 2023, 2024, 2025]
subjs = ["математика", "русский/белорусский язык", "иностранный язык",
         "физика", "биология", "химия", "история", "общество"]
specs = [
    "Информационные системы и технологии",
    "Искусственный интеллект",
    "Стоматология",
    "Фармация",
    "Экономика",
    "Менеджмент",
    "Финансы и кредит",
    "Бухгалтерский учет",
    "Психология",
    "Международные отношения",
]
forms = ["Бюджет", "Платное", "Целевое"]
regs = ["Брестская", "Витебская", "Гродненская", "Гомельская", "Минская", "Могилевская", "Минск"]

def generate_data(num_stud=500):
    students = []

    for _ in range(num_stud):
        year = random.choice(years)
        specialty = random.choice(specs)
        education_form = random.choice(forms)
        region = random.choice(regs)

        ct_scores = {}
        for subject in subjs:
            score = random.randint(55, 95)
            ct_scores[subject] = score

        avg_certificate = round(random.uniform(6.5, 9.0), 1)

        best_ct_scores = sorted(ct_scores.values(), reverse=True)[:3]
        total_score = sum(best_ct_scores) + avg_certificate * 10

        student = {
            'ФИО': fake.name(),
            'Год_поступления': year,
            'Форма_обучения': education_form,
            'Средний_балл_аттестата': avg_certificate,
            'Общий_балл': round(total_score),
            'Специальность': specialty,
            'Регион': region,
            **ct_scores
        }
        students.append(student)

    return pd.DataFrame(students)

print("Генерация данных о вступительной кампании...")
df = generate_data(1000)
print(f"Сгенерировано {len(df)} записей")
print("\nПервые 5 записей:")
print(df.head())
df.to_csv('абитуриенты_2021-2025.csv', index=False, encoding='utf-8-sig')
print("\nДанные сохранены в файл: абитуриенты_2021-2025.csv")

print("\n" + "="*60)
print("ВИЗУАЛИЗАЦИЯ ДАННЫХ ВСТУПИТЕЛЬНОЙ КАМПАНИИ")
print("="*60)

# 1. Динамика среднего балла за ЦТ по предметам
plt.figure(figsize=(15, 12))

plt.subplot(2, 3, 1)
ct_dynamics = df.groupby('Год_поступления')[subjs].mean()
for subject in subjs[:5]:
    plt.plot(ct_dynamics.index, ct_dynamics[subject], marker='o', linewidth=2, label=subject)

plt.title('Динамика среднего балла ЦТ по предметам\n(2021-2025 гг.)', fontsize=12, fontweight='bold')
plt.xlabel('Год поступления')
plt.ylabel('Средний балл')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(years)
plt.grid(True, alpha=0.3)

# 2. Динамика среднего балла аттестата
plt.subplot(2, 3, 2)
certificate_dynamics = df.groupby('Год_поступления')['Средний_балл_аттестата'].mean()
plt.plot(certificate_dynamics.index, certificate_dynamics.values,
         marker='s', color='red', linewidth=3, markersize=6)
plt.title('Динамика среднего балла аттестата\n(2021-2025 гг.)', fontsize=12, fontweight='bold')
plt.xlabel('Год поступления')
plt.ylabel('Средний балл аттестата')
plt.xticks(years)
plt.grid(True, alpha=0.3)

# 3. Количество поступивших по специальностям
plt.subplot(2, 3, 3)
specialty_counts = df['Специальность'].value_counts()
colors = plt.cm.Set3(range(len(specialty_counts)))
bars = plt.bar(specialty_counts.index, specialty_counts.values, color=colors)

plt.title('Количество поступивших по специальностям\n(2021-2025 гг.)', fontsize=12, fontweight='bold')
plt.xlabel('Специальность')
plt.ylabel('Количество студентов')
plt.xticks(rotation=45, ha='right')

# Добавляем значения на столбцы
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 3,
             f'{int(height)}', ha='center', va='bottom', fontsize=9)

# 4. Статистика по формам обучения
plt.subplot(2, 3, 4)
form_counts = df['Форма_обучения'].value_counts()
colors = ['#ff9999', '#66b3ff', '#99ff99']
plt.pie(form_counts.values, labels=form_counts.index, autopct='%1.1f%%',
        startangle=90, colors=colors, shadow=True)
plt.title('Распределение по формам обучения', fontsize=12, fontweight='bold')

# 5. Средний общий балл по специальностям
plt.subplot(2, 3, 5)
specialty_scores = df.groupby('Специальность')['Общий_балл'].mean().sort_values(ascending=False)
plt.bar(specialty_scores.index, specialty_scores.values, color='lightblue')
plt.title('Средний общий балл по специальностям', fontsize=12, fontweight='bold')
plt.xlabel('Специальность')
plt.ylabel('Средний общий балл')
plt.xticks(rotation=45, ha='right')

# 6. Распределение студентов по регионам
plt.subplot(2, 3, 6)
region_counts = df['Регион'].value_counts()
plt.bar(region_counts.index, region_counts.values, color='orange')
plt.title('Распределение студентов по регионам', fontsize=12, fontweight='bold')
plt.xlabel('Регион')
plt.ylabel('Количество студентов')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# 7. Боксплот распределения баллов по специальностям (без seaborn)
plt.figure(figsize=(12, 6))

# Создаем boxplot вручную с помощью matplotlib
specialties = df['Специальность'].unique()
data_to_plot = []

for specialty in specialties:
    specialty_data = df[df['Специальность'] == specialty]['Общий_балл']
    data_to_plot.append(specialty_data)

plt.boxplot(data_to_plot, labels=specialties)
plt.title('Распределение общего балла по специальностям', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Общий балл')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 8. Тепловая карта корреляции предметов (без seaborn)
plt.figure(figsize=(10, 8))
correlation_matrix = df[subjs].corr()

# Создаем тепловую карту с помощью imshow
plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)

# Добавляем значения в ячейки
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                ha='center', va='center', fontsize=10)

plt.colorbar(label='Корреляция')
plt.xticks(range(len(subjs)), subjs, rotation=45, ha='right')
plt.yticks(range(len(subjs)), subjs)
plt.title('Корреляция баллов по предметам ЦТ', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

# СТАТИСТИКА

print("\n" + "="*60)
print("СТАТИСТИЧЕСКАЯ ИНФОРМАЦИЯ")
print("="*60)

print(f" Общее количество студентов: {len(df)}")
print(f" Период данных: {df['Год_поступления'].min()}-{df['Год_поступления'].max()} гг.")
print(f" Количество специальностей: {df['Специальность'].nunique()}")

print(f"\n Средние баллы за ЦТ по предметам (2025 год):")
df_2025 = df[df['Год_поступления'] == 2025]
for subject in subjs:
    mean_score = df_2025[subject].mean()
    print(f"  {subject}: {mean_score:.1f}")

print(f"\n Средний балл аттестата: {df['Средний_балл_аттестата'].mean():.1f}")
print(f" Средний общий балл: {df['Общий_балл'].mean():.1f}")

print(f"\n Распределение по формам обучения:")
for form, count in df['Форма_обучения'].value_counts().items():
    percentage = (count / len(df)) * 100
    print(f"  {form}: {count} студентов ({percentage:.1f}%)")

print(f"\n Топ-3 специальности по количеству студентов:")
for i, (spec, count) in enumerate(df['Специальность'].value_counts().head(3).items(), 1):
    percentage = (count / len(df)) * 100
    print(f"  {i}. {spec}: {count} студентов ({percentage:.1f}%)")

print(f"\n Распределение по регионам:")
for i, (region, count) in enumerate(df['Регион'].value_counts().head(3).items(), 1):
    percentage = (count / len(df)) * 100
    print(f"  {i}. {region}: {count} студентов ({percentage:.1f}%)")

# СВОДНАЯ ТАБЛИЦА

print("\n" + "="*60)
print("СВОДНАЯ СТАТИСТИКА ПО ГОДАМ")
print("="*60)

yearly_stats = df.groupby('Год_поступления').agg({
    'Общий_балл': ['mean', 'min', 'max'],
    'Средний_балл_аттестата': 'mean',
    'ФИО': 'count'
}).round(1)

yearly_stats.columns = ['Ср.общий_балл', 'Мин.балл', 'Макс.балл', 'Ср.аттестат', 'Кол-во_студентов']
print(yearly_stats)

yearly_stats.to_csv('сводная_статистика_2021_2025.csv', encoding='utf-8-sig')
print("\n Сводная статистика сохранена в файл: сводная_статистика_2021_2025.csv")

print("АНАЛИЗ ЗАВЕРШЕН! ")
