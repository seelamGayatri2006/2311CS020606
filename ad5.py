import pandas as pd

# Create the Patient Information DataFrame
patient_data = {
    'Patient Name': ['John Doe', 'Jane Smith', 'Tom Brown', 'Lucy Green'],
    'Age': [4, 6, 5, 3],
    'Date of Appointment': ['2025-01-15', '2025-01-16', '2025-01-17', '2025-01-18'],
    'Patient ID': [101, 102, 103, 104]
}
patient_info = pd.DataFrame(patient_data)

# Create the Drug Quantity DataFrame
drug_data = {
    'Drug Name': ['Aspirin', 'Penicillin', 'Aspirin', 'Tylenol'],
    'Quantity': [2, 3, 1, 5],
    'Patient ID': [101, 102, 103, 104]
}
drug_quantity = pd.DataFrame(drug_data)

# Filter patient info for patients with age < 6, keeping Patient ID
filtered_patients = patient_info[patient_info['Age'] < 6][['Patient Name', 'Age', 'Patient ID']]

# Merge the two DataFrames using an inner join on 'Patient ID'
merged_data = pd.merge(filtered_patients, drug_quantity, on='Patient ID', how='inner')

# Display the merged DataFrame
print(merged_data)
