import pandas as pd

# Load the dataset
file_path = r'C:\Users\AKHILA\OneDrive\Desktop\mini_proj\sample_google_analytics_data.csv'
data = pd.read_csv(file_path)

# Function for noise reduction
def reduce_noise(data, pageviews_threshold=20, sessions_threshold=15, users_threshold=10):

    # Filter rows based on thresholds
    filtered_data = data[
        (data['pageviews'] >= pageviews_threshold) &
        (data['sessions'] >= sessions_threshold) &
        (data['users'] >= users_threshold)
    ]
    
    # Sort the filtered data for easier analysis
    filtered_data = filtered_data.sort_values(by='pageviews', ascending=False).reset_index(drop=True)
    
    return filtered_data

# Apply the noise-reduction function to the dataset
cleaned_data = reduce_noise(data)

# Display the cleaned data
print("Cleaned Data:")
print(cleaned_data)
