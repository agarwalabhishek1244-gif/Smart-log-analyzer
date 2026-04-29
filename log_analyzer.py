import pandas as pd
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Load sample logs
df = pd.read_csv("sample_logs.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Count log levels
print("Log Level Count:")
print(df["level"].value_counts())

# Filter errors
errors = df[df["level"] == "ERROR"]
print("\nError Logs:")
print(errors)

# Prepare log text for AI
log_text = df["message"].to_string()

# AI Insights
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f"Analyze these logs and give insights:\n{log_text}"}
    ]
)

print("\nAI Insights:")
print(response.choices[0].message.content)