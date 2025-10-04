#10
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def average_death_confirmed_ratio(df, threshold):
    filtered = df[df["Active"] > threshold]
    if filtered.empty:
        return None
    ratio = filtered["Deaths"] / filtered["Confirmed"]
    return ratio.mean()

def main():
    df = load_data("covid.csv")
    thresholds = [500, 1000, 5000]
    for t in thresholds:
        avg_ratio = average_death_confirmed_ratio(df, t)
        if avg_ratio is not None:
            print(f"Average death/confirmed ratio for countries with more than {t} active cases: {avg_ratio:.4f}")
        else:
            print(f"No countries with more than {t} active cases")

if __name__ == "__main__":
    main()

        
