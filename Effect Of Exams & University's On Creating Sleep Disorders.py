import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('Data.csv')

# Creating the bar chart of te effect of external factors on academic developpemnt
column_data = df["6. Do you experience any sleep disorders during exams and assesment due to the university environment ?"]
dissatisfaction_levels = ["always", "not much", "sometimes", "occasionally", "never"]
dissatisfaction_counts = {level: 0 for level in dissatisfaction_levels}
for level in dissatisfaction_levels:
    dissatisfaction_counts[level] = column_data.str.contains(level).sum()
total_responses = len(column_data)
plt.figure(figsize=(10, 6))
bars = plt.bar(dissatisfaction_counts.keys(), dissatisfaction_counts.values(), color='skyblue')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), 
             ha='center', va='bottom', fontsize=10)
plt.xlabel('Effect Levels')
plt.ylabel('Count')
plt.title('Effect Of Exams & University On Creating Sleep Disorders')
plt.xticks(rotation=45)
plt.text(0, max(dissatisfaction_counts.values()) + 5, f"Total Responses: {total_responses}", ha='left')
plt.tight_layout()
plt.show()
