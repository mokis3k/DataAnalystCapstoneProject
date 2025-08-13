import pandas as pd


input_file = "m5_survey_data_demographics.csv"
output_file = "job_factors_count.csv"

# reading file
df = pd.read_csv(input_file)

# column name
if "JobFactors" not in df.columns:
    raise ValueError("В файле нет колонки 'JobFactors'!")

# filling up missing values
df["JobFactors"] = df["JobFactors"].fillna("")

# Spliting by delimeter
factors = (
    df["JobFactors"]
    .str.split(";")
    .explode()
    .str.strip()
)

# Clearing missing values
factors = factors[factors != ""]

# Every factor counts
counts = factors.value_counts().reset_index()
counts.columns = ["JobFactors", "Count"]

# Saving to CSV file
counts.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Готово! Результат сохранён в {output_file}")
