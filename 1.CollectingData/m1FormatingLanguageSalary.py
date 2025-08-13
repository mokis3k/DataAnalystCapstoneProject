import pandas as pd


input_file = "popular-languages.csv"
output_file = "popular-languages-clean.csv"

# reading file
df = pd.read_csv(input_file)

# column name
salary_col = "Average Annual Salary"

# checking existing column
if salary_col not in df.columns:
    raise ValueError(f"В файле нет колонки '{salary_col}'!")

# deleting commas, changing "$" symbol
df[salary_col] = (
    df[salary_col]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Готово! Числовые значения зарплат сохранены в {output_file}")
