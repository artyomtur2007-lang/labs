import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('lab_4_part_5.xlsx', header=1)

df = df.drop('Unnamed: 0', axis=1)
df.columns = ['дата', 'год', 'год-мес', 'точка', 'бренд', 'товар', 'количество', 'продажи', 'себестоимость']

print(" АНАЛИЗ ПРОДАЖ")
print(f"Всего записей: {len(df)}")
print(f"Товаров: {df['товар'].nunique()}")
print(f"Точек продаж: {df['точка'].nunique()}")

df['Прибыль'] = df['продажи'] - df['себестоимость']
df['Средняя_цена'] = df['продажи'] / df['количество']

print(f"\nОбщие продажи: {df['продажи'].sum():,.0f} руб")
print(f"Общая прибыль: {df['Прибыль'].sum():,.0f} руб")

# продажи по месяцам
print("\nПродажи по месяцам:")
monthly_sales = df.groupby('год-мес')['продажи'].sum()
print(monthly_sales)

plt.figure(figsize=(12, 4))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')
plt.title('Продажи по месяцам')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# продажи по товарам
print("\nПродажи по товарам:")
sales_by_product = df.groupby('товар')['продажи'].sum().sort_values(ascending=False)
print(sales_by_product)

plt.figure(figsize=(10, 4))
plt.bar(sales_by_product.index, sales_by_product.values)
plt.title('Продажи по товарам')
plt.xticks(rotation=45)
plt.show()

# продажи по точкам
print("\n Продажи по точкам:")
sales_by_point = df.groupby('точка')['продажи'].sum().sort_values(ascending=False)
print(sales_by_point)

plt.figure(figsize=(8, 4))
plt.bar(sales_by_point.index, sales_by_point.values, color='green')
plt.title('Продажи по точкам')
plt.xticks(rotation=45)
plt.show()

# статистика по товарам
print("СТАТИСТИКА ПО ТОВАРАМ")
for product in df['товар'].unique():
    product_data = df[df['товар'] == product]
    total_sales = product_data['продажи'].sum()
    avg_price = product_data['Средняя_цена'].mean()
    total_profit = product_data['Прибыль'].sum()
    print(f"{product}:")
    print(f"  Продажи: {total_sales:,.0f} руб")
    print(f"  Средняя цена: {avg_price:.0f} руб")
    print(f"  Прибыль: {total_profit:,.0f} руб")
    print()

# прогноз
if not monthly_sales.empty:
    forecast_sales = monthly_sales.tail(3).mean()
    print("ПРОГНОЗ")
    print(f"Прогноз объема продаж на следующий месяц: {forecast_sales:,.0f} руб")

    plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', color='blue')
    plt.axhline(y=forecast_sales, color='red', linestyle='--')
    plt.title("Прогноз продаж")
    plt.grid(True, alpha=0.3)
    plt.show()

