import pandas as pd


input_file = "m5_survey_data_demographics.csv"
output_file = "job_factors_count.csv"

# reading file
df = pd.read_csv(input_file)

# column name
if "JobFactors" not in df.columns:
    raise ValueError("no column JobFactors)

# filling up missing values
df["JobFactors"] = df["JobFactors"].fillna("")

# spliting by delimeter
factors = (
    df["JobFactors"]
    .str.split(";")
    .explode()
    .str.strip()
)

# clearing missing values
factors = factors[factors != ""]

# every factor counts
counts = factors.value_counts().reset_index()
counts.columns = ["JobFactors", "Count"]

# saving to CSV file
counts.to_csv(output_file, index=False, encoding="utf-8-sig")

print(output_file)
