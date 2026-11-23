# Задание 1
import pandas as pd

players = {
    "name":   ["Tom", "Arina", "Ivan", "Dasha", "Danya", "Ilya"],
    "level":  [60, 51, 52, 78, 71, 33],
    "klass":  ["Воин", "Маг", "Шаман", "Лучник", "Демонолог", "Паладин"],
    "donate": [400, 1100, 200, 2300, 1700, 250]
}

df = pd.DataFrame(players)
print(df.head(2))

# Задание 2
df.to_csv("dataset.csv", index=False, encoding="utf-8")

df2 = pd.read_csv("dataset.csv", encoding="utf-8")
df2.info()

# Задание 3
result = df[(df["level"] > 50) & (df["klass"] == "Маг")]
print(result)

# Задание 4
top = df.sort_values("donate", ascending=False)
print(top.head(3))




