salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

while True:
    delta = spend - salary  # находим расзницу в затратах и прибыли
    months -= 1  # уменьшение количества месяцев
    if months < 0:  # цикл остановится когда закончатся месяцы
        break

    money_capital += delta  # прибавляем затраты за месяц, чтобы понять сколько средств нам необходимо
    spend *= 1 + increase


print(round(money_capital))
