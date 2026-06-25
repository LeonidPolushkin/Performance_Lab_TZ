"""
На вход в качестве аргументов программы поступают три пути к файлу (в приложении к заданию находятся примеры этих файлов):
●	values.json содержит результаты прохождения тестов с уникальными id
●	tests.json содержит структуру для построения отчета на основе прошедших тестов (вложенность может быть большей, чем в примере)
●	report.json - сюда записывается результат.
Напишите программу, которая формирует файл report.json с заполненными полями value для структуры tests.json на основании values.json.
Структура report.json такая же, как у tests.json, только заполнены поля “value”.

На вход программы передается три пути к файлу!
"""

import json
import sys

with open(sys.argv[1]) as v:
    values = json.load(v)["values"]

values_by_id = {v["id"] : v["value"] for v in values}

with open(sys.argv[2]) as t:
    tests = json.load(t)

def fill_value(val, fill):
    for i in range(len(val)):
        val_id = val[i]["id"]
        if "value" in val[i]:
            val[i]["value"] = fill[val_id]
        if "values" in val[i]:
            fill_value(val[i]["values"], fill)

fill_value(tests["tests"], values_by_id)

with open(sys.argv[3], "w") as r:
    json.dump(tests, r, indent=2)