
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def analyze_grades(df):
    summary = {
        "average": df["Grade"].mean(),
        "max": df["Grade"].max(),
        "min": df["Grade"].min(),
        "passed": (df["Grade"] >= 50).sum(),
        "failed": (df["Grade"] < 50).sum()
    }
    return summary

def add_letter_grades(df):
    def get_letter(grade):
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'
    df["Letter"] = df["Grade"].apply(get_letter)
    return df

def main():
    df = load_data("data.csv")
    df = add_letter_grades(df)
    summary = analyze_grades(df)

    print("=== Grade Summary ===")
    for k, v in summary.items():
        print(f"{k}: {v}")

    df.to_csv("output.csv", index=False)
    print("\nProcessed data saved to output.csv")

if __name__ == "__main__":
    main()
