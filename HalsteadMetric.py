import re
import math

operators = [
    "import",
    "from",
    "for",
    "def",
    "return",
    "try",
    "while",
    "match",
    "case",
    "if",
    "or",
    "break",
    "except",
    "range",
    "len",
    "int",
    "input",
    "print",
    "abs",
    "str",
    "f\"",
    "split",
    "random.randint",
    "decimal.Decimal",
    "sqrt",
    "tan",
    "sin",
    "input_matrix",
    "random_init",
    "print_matrix",
    "items",
    "Y",
    "=",
    "==",
    "<=",
    ">=",
    "+=",
    "+",
    "-",
    "*",
    "/",
    "**",
    "["
]

operands = [
    "glen",
    "mlen",
    "nlen",
    "0",
    "1",
    "2",
    "4",
    "5",
    "6",
    "g",
    "m",
    "n",
    "_",
    "matrix",
    "n",
    "i",
    "s",
    "k",
    "j",
    "left",
    "right",
    "x",
    "a",
    "b",
    "d",
    "c",
    "t",
    "ab",
    "dc",
    "tk",
    "Выберите_способ задания_матриц:",
    "1 - ручной ввод",
    "2 - автоматический ввод",
    "ch",
    "Введите матрицу g",
    "Введите матрицу m",
    "Введите матрицу n",
    "-1000",
    "1000",
    "Неверный ввод, повторите попытку",
    "Матрица g:",
    "Матрица m:",
    "Матрица n:",
    "a = ",
    ", b = ",
    "d = ",
    ", c = ",
    "t = ",
    ", k = ",
    "Введите xs, st и h:",
    "xs",
    "xt",
    "h",
    "table",
    "key",
    "value",
    "Деление на ноль!",
    "Выход за пределы массива"
]

operators_count = {i: 0 for i in operators}
operands_count = {i: 0 for i in operands}

# Открываем файл на чтение
with open("main.py", "r", encoding="UTF-8") as file:
    code = file.read()

# Считаем количество операторов
for operator in operators:
    operators_count[operator] = len(re.findall(r'\b' + re.escape(operator) + r'\b', code))

# Считаем количество операндов
for operand in operands:
    operands_count[operand] = len(re.findall(r'\b' + re.escape(operand) + r'\b', code))

# Вычисляем суммы
total_operators = sum(operators_count.values())
total_operands = sum(operands_count.values())

print("Количество операторов:")
for operator, count in operators_count.items():
    print(f"{operator}: {count}")

print("Количество операндов:")
for operand, count in operands_count.items():
    print(f"{operand}: {count}")

print("Общее количество операторов:", total_operators)
print("Общее количество операндов:", total_operands)

# Вычисляем объём
V = (total_operands + total_operators) * math.log(len(operators) + len(operands),2)
print("Объем программы: ", V)




