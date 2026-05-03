import pandas as pd

def process_data(df):
    # Step 1: Remove missing values
    df = df.dropna()

    # Step 2: Add GST (simulate processing)
    df["amount_with_gst"] = df["amount"] * 1.18

    # Step 3: Add category (basic logic)
    df["category"] = df["amount"].apply(lambda x: "High" if x > 500 else "Low")

    return df


if __name__ == "__main__":
    # Sample data (same as ingestion)
    data = {
        "customer": ["A", "B", "C"],
        "amount": [500, 700, 300]
    }

    df = pd.DataFrame(data)

    processed_df = process_data(df)

    print(processed_df)