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

#Описательные статистики
print("\n=== Описательные статистики ===")
print(df.describe())

#Активные аэропорты
def plot_top_airports(column, title, color):
    top = df[column].value_counts().head(10)
    if not top.empty:
        plt.bar(top.index, top.values, color=color)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.ylabel("Количество рейсов")
        plt.tight_layout()
        plt.show()
    else:
        print(f"Нет данных для {title}")

plot_top_airports('ORIG_CITY_CODE', "Топ-10 аэропортов отправления", 'skyblue')
plot_top_airports('DEST_CITY_CODE', "Топ-10 аэропортов назначения", 'lightgreen')

#  Сезонность
monthly_sales = df.groupby(['YEAR', 'MONTH'])['REVENUE_AMOUNT'].sum().unstack()
if not monthly_sales.empty:
    monthly_sales.plot(marker='o', figsize=(10,5), grid=True)
    plt.title("Сезонность по выручке")
    plt.xlabel("Месяц")
    plt.ylabel("Сумма продаж")
    plt.tight_layout()
    plt.show()
else:
    print("Нет данных для сезонности по выручке")

monthly_flights = df.groupby(['YEAR', 'MONTH']).size().unstack()
if not monthly_flights.empty:
    monthly_flights.plot(marker='o', figsize=(10,5), grid=True)
    plt.title("Сезонность по количеству перелетов")
    plt.xlabel("Месяц")
    plt.ylabel("Количество перелетов")
    plt.tight_layout()
    plt.show()
else:
    print("Нет данных для сезонности по перелётам")

#  Типы пассажиров и FFP
if 'PAX_TYPE' in df.columns and df['PAX_TYPE'].notna().any():
    df.boxplot(column='REVENUE_AMOUNT', by='PAX_TYPE', grid=True)
    plt.title("Выручка по типу пассажира")
    plt.suptitle("")
    plt.xlabel("Тип пассажира")
    plt.ylabel("Сумма покупки")
    plt.tight_layout()
    plt.show()
else:
    print("Нет данных по типам пассажиров")

if 'FFP_FLAG' in df.columns:
    ffp_stats = df.groupby('FFP_FLAG')['REVENUE_AMOUNT'].mean()
    print("\nСредняя выручка по FFP статусу:")
    print(ffp_stats)

# Способы оплаты
df_clean = df.dropna(subset=['FOP_TYPE_CODE', 'REVENUE_AMOUNT'])
fop_avg = df_clean.groupby('FOP_TYPE_CODE')['REVENUE_AMOUNT'].mean().sort_values()

plt.bar(fop_avg.index.astype(str), fop_avg.values, color='mediumseagreen')
plt.title("Сумма покупки по способу оплаты")
plt.ylabel("Сумма")
plt.xlabel("Способ оплаты")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()








