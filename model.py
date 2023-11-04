from sklearn.cluster import KMeans
from load import diabetes_df
# Prepare the data for K-means (select relevant columns)
# Adjust 'X_columns' to the columns you want to use for clustering
X_columns = ['BloodPressure','Glucose','BMI']
X = diabetes_df[X_columns]

# K-means clustering with k=3
kmeans = KMeans(n_clusters=3)
diabetes_df['cluster'] = kmeans.fit_predict(X)

# Count the number of records in each cluster
cluster_counts = diabetes_df['cluster'].value_counts()

# Save cluster counts as a text file
cluster_counts.to_csv('k.txt', header=['count'], index_label='cluster', sep='\t')

print("K-means clustering completed.")
