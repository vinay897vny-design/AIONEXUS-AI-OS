import pandas as pd

def generate_report(df):
    print("\n--- MIS REPORT ---")

    # Total revenue
    total = df["amount"].sum()
    print("Total Revenue:", total)

    # Average revenue
    avg = df["amount"].mean()
    print("Average Revenue:", avg)

    # High value customers
    high = df[df["amount"] > 500]
    print("\nHigh Value Customers:")
    print(high)

    # Insight
    if avg > 500:
        print("\nInsight: Business is performing well")
    else:
        print("\nInsight: Business needs improvement")


if __name__ == "__main__":
    data = {
        "customer": ["A", "B", "C"],
        "amount": [500, 700, 300]
    }

    df = pd.DataFrame(data)

    generate_report(df)