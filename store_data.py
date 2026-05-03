import pandas as pd

def store_data():
    # sample processed data
    data = {
        "customer": ["A", "B", "C"],
        "amount": [500, 700, 300]
    }

    df = pd.DataFrame(data)

    # simulate ERP storage
    df.to_json("erp_data.json", orient="records", indent=4)

    print("✅ Data stored in ERP layer (JSON file created)")

if __name__ == "__main__":
    store_data()