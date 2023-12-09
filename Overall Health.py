import pandas as pd
import matplotlib.pyplot as plt
import statistics
#Read the CSV file into a DataFrame
df = pd.read_csv('Data.csv')
#Creating the pie chart for the Overall Health
column_data = df["7. How do you rate your overall health ?"]
tab = pd.to_numeric(column_data, errors='coerce').dropna().astype(int)
value_counts = tab.value_counts()
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Overall Health')
plt.axis('equal')
total_responses = len(tab)
legend_labels = [f"{label} ({value_counts[label]})" for label in value_counts.index]
legend_labels.append(f"Total Responses: {total_responses}")
plt.legend(legend_labels, loc="best")
plt.text(1.5, 0.5, f"Total Responses: {total_responses}", fontsize=12, verticalalignment='center')
plt.show()
# Calculate statistics
mean_value = statistics.mean(tab)
median_value = statistics.median(tab)
mode_value = statistics.mode(tab)
std_dev = statistics.stdev(tab)
print(f"Average Response: {mean_value}")
print(f"Median Value: {median_value}")
print(f"Mode (Frequent Responses): {mode_value}")