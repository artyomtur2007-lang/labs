import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('lab_4_part_5.xlsx', header=1)

df = df.drop('Unnamed: 0', axis=1)
df.columns = ['дата', 'год', 'год-мес', 'точка', 'бренд', 'товар', 'количество', 'продажи', 'себестоимость']

print("=== ПРОСТОЙ АНАЛИЗ ПРОДАЖ ===")
print(f"Всего записей: {len(df)}")
print(f"Товаров: {df['товар'].nunique()}")
print(f"Точек продаж: {df['точка'].nunique()}")

df['Прибыль'] = df['продажи'] - df['себестоимость']
df['Средняя_цена'] = df['продажи'] / df['количество']

print(f"\nОбщие продажи: {df['продажи'].sum():,.0f} руб")
print(f"Общая прибыль: {df['Прибыль'].sum():,.0f} руб")

# продажи по месяцам
print("\n1. График продаж по месяцам")
monthly_sales = df.groupby('год-мес')['продажи'].sum()
plt.figure(figsize=(12, 4))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')
plt.title('Продажи по месяцам')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# продажи по товарам
print("2. График продаж по товарам")
sales_by_product = df.groupby('товар')['продажи'].sum()
plt.figure(figsize=(10, 4))
plt.bar(sales_by_product.index, sales_by_product.values)
plt.title('Продажи по товарам')
plt.xticks(rotation=45)
plt.show()

# продажи по точкам
print("3. График продаж по точкам")
sales_by_point = df.groupby('точка')['продажи'].sum()
plt.figure(figsize=(8, 4))
plt.bar(sales_by_point.index, sales_by_point.values, color='green')
plt.title('Продажи по точкам')
plt.xticks(rotation=45)
plt.show()

print("\n=== СТАТИСТИКА ПО ТОВАРАМ ===")
for product in df['товар'].unique():
    product_data = df[df['товар'] == product]
    total_sales = product_data['продажи'].sum()
    avg_price = product_data['Средняя_цена'].mean()
    print(f"{product}:")
    print(f"  Продажи: {total_sales:,.0f} руб")
    print(f"  Средняя цена: {avg_price:.0f} руб")
    print()

print("=== АНАЛИЗ ЗАВЕРШЕН ===")