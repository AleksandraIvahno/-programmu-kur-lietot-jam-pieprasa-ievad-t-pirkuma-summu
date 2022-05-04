# Эта функция проверит сколько покупатель должен заплатить со скидкой
def checkPay(sum):
  # 10% скидка от суммы покупки
  atlaide = 0.1
  # заранее создать переменную чтобы потом её показать
  mustPay = 0

  # если у покупателя сумма больше чем или равно 200 евро
  if sum >= 200:
    withSale = sum * 0.1
    mustPay = sum - withSale
  else:
    # иначе, просто показать ту же сумму
    mustPay = sum
  return mustPay


summa = int(input("Ievadiet pirkuma summu: "))
print("Jūsu konts:", checkPay(summa), "eiro")
