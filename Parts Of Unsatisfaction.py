import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('Data.csv')

# Creating the bar chart of the dissatisfaction levels
column_data = df["5. What is the part of your student life that you are unsatisfied with the most?"]
dissatisfaction_levels = ["Social life", "Teacher", "Subjects", "Schedule", "Exams", "Administration"]
dissatisfaction_counts = {level: 0 for level in dissatisfaction_levels}
for level in dissatisfaction_levels:
    dissatisfaction_counts[level] = column_data.str.contains(level).sum()
total_responses = len(column_data)
plt.figure(figsize=(10, 6))
bars = plt.bar(dissatisfaction_counts.keys(), dissatisfaction_counts.values(), color='skyblue')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), 
             ha='center', va='bottom', fontsize=10)

plt.xlabel('Dissatisfaction Levels')
plt.ylabel('Count')
plt.title('Number of Dissatisfaction Levels')
plt.xticks(rotation=45)
plt.text(0, max(dissatisfaction_counts.values()) + 5, f"Total Responses: {total_responses}", ha='left')
plt.tight_layout()
plt.show()
