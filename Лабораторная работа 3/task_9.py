salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    delta = spend - salary  # находим расзницу в затратах и прибыли
    money_capital += delta  # прибавляем затраты за месяц, чтобы понять сколько средств нам необходимо
    spend *= 1 + increase

print(round(money_capital))
