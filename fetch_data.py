import pandas as pd

def load_data():
    # sample data (instead of real ERP)
    data = {
        "customer": ["A", "B", "C"],
        "amount": [500, 700, 300]
    }
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df)