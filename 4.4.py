import pandas as pd
import matplotlib.pyplot as plt

file_path = "s7_data_sample_rev4_50k.xlsx"
df = pd.read_excel(file_path)

df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'], errors='coerce')
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'], errors='coerce')
df.dropna(subset=['FLIGHT_DATE_LOC', 'REVENUE_AMOUNT'], inplace=True)

df['MONTH'] = df['FLIGHT_DATE_LOC'].dt.month
df['YEAR'] = df['FLIGHT_DATE_LOC'].dt.year
df['WEEKDAY'] = df['FLIGHT_DATE_LOC'].dt.day_name()

# Общие описательные статистики
print("Описательные статистики ")
print(df.describe())

# Активные аэропорты
def plot_top_airports(column, title, color):
    top = df[column].value_counts().head(10)
    print(f"\n{title}:")
    print(top)
    plt.bar(top.index, top.values, color=color)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.ylabel("Количество рейсов")
    plt.tight_layout()
    plt.show()
    most_popular=top.idxmax()
    print(f"Самый популярный: {most_popular}")

plot_top_airports('ORIG_CITY_CODE', "Топ-10 аэропортов отправления", 'skyblue')
plot_top_airports('DEST_CITY_CODE', "Топ-10 аэропортов назначения", 'lightgreen')

# Сезонность по выручке
monthly_sales = df.groupby(['YEAR', 'MONTH'])['REVENUE_AMOUNT'].sum()
if not monthly_sales.empty:
    x_sales = [year + month / 12 for year, month in monthly_sales.index]
    y_sales = monthly_sales.values
    print("\nСезонность по выручке:")
    print(monthly_sales)
    plt.plot(x_sales, y_sales, marker='o', color='red')
    plt.title("Сезонность по выручке")
    plt.xlabel("Год.месяц")
    plt.ylabel("Сумма продаж")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    max_month = monthly_sales.idxmax()
    print(f"Максимальная выручка была в {max_month[1]}.{max_month[0]}")
else:
    print("Нет данных для сезонности по выручке")

#Сезонность по количеству перелетов
monthly_flights = df.groupby(['YEAR', 'MONTH']).size()
if not monthly_flights.empty:
    x_flights = [year + month / 12 for year, month in monthly_flights.index]
    y_flights = monthly_flights.values
    print("\nСезонность по количеству перелетов:")
    print(monthly_flights)
    plt.plot(x_flights, y_flights, marker='o', color='orange')
    plt.title("Сезонность по количеству перелетов")
    plt.xlabel("Год.месяц")
    plt.ylabel("Количество перелетов")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    max_month_flights = monthly_flights.idxmax()
    print(f"Больше всего перелётов было в {max_month_flights[1]}.{max_month_flights[0]}")
else:
    print("Нет данных для сезонности по перелётам")

#Типы пассажиров
if 'PAX_TYPE' in df.columns and df['PAX_TYPE'].notna().any():
    pax_avg = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].mean().sort_values()
    print("\nСредняя выручка по типам пассажиров:")
    print(pax_avg)
    plt.bar(pax_avg.index, pax_avg.values, color='blue')
    plt.title("Средняя выручка по типу пассажира")
    plt.xlabel("Тип пассажира")
    plt.ylabel("Сумма покупки")
    plt.grid(True, axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    best_pax = pax_avg.idxmax()
    print(f"Самый прибыльный тип:{best_pax}")
else:
    print("Нет данных по типам пассажиров")

#FFP статус
if 'FFP_FLAG' in df.columns:
    ffp_stats = df.groupby('FFP_FLAG')['REVENUE_AMOUNT'].mean()
    print("\nСредняя выручка по FFP статусу:")
    print(ffp_stats)
    best_ffp = ffp_stats.idxmax()
    print(f"Наибольшая средняя выручка у  {best_ffp}")

# Способы оплаты
df_clean = df.dropna(subset=['FOP_TYPE_CODE', 'REVENUE_AMOUNT'])
fop_avg = df_clean.groupby('FOP_TYPE_CODE')['REVENUE_AMOUNT'].mean().sort_values()
print("\nСредняя сумма покупки по способам оплаты:")
print(fop_avg)
best_fop=fop_avg.idxmax()
print(f"самый прибльный способ оплаты: {best_fop}")

plt.bar(fop_avg.index.astype(str), fop_avg.values, color='mediumseagreen')
plt.title("Сумма покупки по способу оплаты")
plt.ylabel("Сумма")
plt.xlabel("Способ оплаты")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Прогноз
if not monthly_sales.empty and not monthly_flights.empty:
    forecast_sales = monthly_sales.tail(3).mean()
    forecast_flights = monthly_flights.tail(3).mean()

    print(f"Прогноз объема продаж билетов на следующий месяц: {forecast_sales:.0f}")
    print(f"Прогноз количества перелетов на следующий месяц: {forecast_flights:.0f}")

    x_sales = [year + month / 12 for year, month in monthly_sales.index]
    y_sales = monthly_sales.values
    plt.plot(x_sales, y_sales, marker='o', color='blue')
    plt.axhline(y=forecast_sales, color='red', linestyle='--')
    plt.title("Прогноз продаж")
    plt.grid(True, alpha=0.3)
    plt.show()

    x_flights = [year + month / 12 for year, month in monthly_flights.index]
    y_flights = monthly_flights.values
    plt.plot(x_flights, y_flights, marker='o', color='green')
    plt.axhline(y=forecast_flights, color='red', linestyle='--')
    plt.title("Прогноз перелётов")
    plt.grid(True, alpha=0.3)
    plt.show()

