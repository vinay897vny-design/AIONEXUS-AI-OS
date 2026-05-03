import pandas as pd

# Sample data (same as before)
data = {
    "customer": ["A", "B", "C"],
    "amount": [500, 700, 300]
}

df = pd.DataFrame(data)

def chatbot():
    print("🤖 AI Chatbot Started (type 'exit' to stop)\n")

    while True:
        query = input("You: ").lower()

        if query == "exit":
            print("Chatbot ended.")
            break

        elif "total" in query:
            print("Bot: Total revenue is", df["amount"].sum())

        elif "average" in query:
            print("Bot: Average revenue is", df["amount"].mean())

        elif "high" in query:
            high = df[df["amount"] > 500]
            print("Bot: High value customers:\n", high)

        else:
            print("Bot: Sorry, I don't understand. Try asking about revenue or customers.")

if __name__ == "__main__":
    chatbot()