import numpy as np
cost=np.array([50,38,46,53,49,41,47,39,49,52,40,44])
winter_sum=cost[0]+cost[1]+cost[11]
summer_sum=cost[5]+cost[6]+cost[7]
if winter_sum>summer_sum:
    print('В зимний период')
elif winter_sum<summer_sum:
    print('В летний период')
else:
    print('Затраты одинаковы')
m_cost=np.max(cost)
m_month=np.where(cost==m_cost)[0]
print(f"максимальная сумма: {m_cost},самый затратный месяц: {m_month+1}")