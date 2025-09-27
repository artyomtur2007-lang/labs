base_cost = 24.99
minutes_included = 60
sms_included = 30
gb_included = 1

minutes_used = int(input("Введите количество использованных минут: "))
sms_used = int(input("Введите количество использованных SMS: "))
gb_used = float(input("Введите количество использованного интернет-трафика (ГБ): "))

extra_minutes_cost = 0
extra_sms_cost = 0
extra_gb_cost = 0

if minutes_used > minutes_included:
    extra_minutes = minutes_used - minutes_included
    extra_minutes_cost = extra_minutes * 0.89

if sms_used > sms_included:
    extra_sms = sms_used - sms_included
    extra_sms_cost = extra_sms * 0.59

if gb_used > gb_included:
    extra_mb = (gb_used - gb_included) * 1024  # Convert GB to MB
    extra_gb_cost = extra_mb * 0.79 / 1024  # Cost per GB again

total_extra_cost = extra_minutes_cost + extra_sms_cost + extra_gb_cost
subtotal = base_cost + total_extra_cost
tax = subtotal * 0.02
total_cost = subtotal + tax

print("Базовая сумма:", "{:.2f}".format(base_cost))

if extra_minutes_cost > 0:
    print("Дополнительные минуты:", "{:.2f}".format(extra_minutes_cost))
if extra_sms_cost > 0:
    print("Дополнительные SMS:", "{:.2f}".format(extra_sms_cost))
if extra_gb_cost > 0:
    print("Дополнительный трафик:", "{:.2f}".format(extra_gb_cost))

print("Налог:", "{:.2f}".format(tax))
print("Итоговая сумма:", "{:.2f}".format(total_cost))
