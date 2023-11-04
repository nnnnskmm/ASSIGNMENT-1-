
from load import diabetes_df
from matplotlib import pyplot as plt
# Create a simple visualization (replace with your visualization code)
plt.figure()
plt.plot(diabetes_df['BloodPressure'], diabetes_df['Glucose'])
plt.xlabel('BloodPressure')
plt.ylabel('Glucose')
plt.title('Sample Visualization')
plt.savefig('vis.png')

print("Visualization created.")