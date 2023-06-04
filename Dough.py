"""Программа для подсчета нормы заготовки теста, которая содержит:"""


# 1. ввод шести значений, для подсчета
# 2. формулы расчета
# 3. вывод 'float' результатов
# Тесто dough = d подразделяется на три "диаметра плюшки" (25, 30, 35) и замесы, в которых плюшки хранятся в
# количестве (69, 30, 35):
# 1. Актуальный остаток(rest): 25,30,35 - d_rest_1; d_rest_2; d_rest_3
# 2. Расход теста по сумме (n)-дней(norm): 25,30,35 - d_norm_1; d_norm_2; d_norm_3
# 3. Результат в виде "нормы дня", разницы остатка от нормы(d_norm - d_rest) --> (d_res): 25, 30, 35 - d_res_1; d_res_2;
# d_res_3
# 4. Результат в виде "замесов", частное результата от кол-ва плюшек в замесе(k_res): 25, 30, 35 - k_res_1; k_res_2;
# k_res_3

# noinspection PyGlobalUndefined
def calculation():
    global d_type, mul_1, mul_2, mul_3
    # calculation_method = cal_meth
    cal_meth = int(input('Сделать расчет в лотках - 1, в замесах - 2: '))

    # multiplier: mul_1, mul_2, mul_3
    if cal_meth == 1:
        d_type = 'лотках'
        [mul_1, mul_2, mul_3] = 10, 7, 5
    elif cal_meth == 2:
        d_type = 'замесах'
        [mul_1, mul_2, mul_3] = 70, 49, 35
    elif cal_meth != 1 or 2:
        print('Необходимо ввести число 1 или 2.')
        calculation()

    d_list = d_rest_25, d_rest_30, d_rest_35 = [int(input(f"Остаток в {d_type} 25:")) * (int(f'{mul_1}')),
                                                int(input(f"Остаток в {d_type} 30:")) * (int(f'{mul_2}')),
                                                int(input(f"Остаток в {d_type} 35:")) * (int(f'{mul_3}'))]
    for dough in d_list:
        print("Остаток в плюшках: " + str(dough))

    d_norm_25, d_norm_30, d_norm_35 = [int(input("Расход по 25: ")),
                                       int(input("Расход по 30: ")),
                                       int(input("Расход по 35: "))]

    d_res_25, d_res_30, d_res_35 = [d_norm_25 - d_rest_25,
                                    d_norm_30 - d_rest_30,
                                    d_norm_35 - d_rest_35]

    k_res_25, k_res_30, k_res_35 = [round(d_res_25 / 69, 1),
                                    round(d_res_30 / 47, 1),
                                    round(d_res_35 / 35, 1)]

    result = [k_res_25, k_res_30, k_res_35]

    for res in result:
        if res > 0:
            print("В запасе: \n" + str(res))
        elif res < 0:
            print("Надо сделать: \n" + str(res))
        elif res == 0:
            print("По нулям: \n" + str(res))


calculation()
