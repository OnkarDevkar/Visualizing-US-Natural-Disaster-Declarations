# This script is responsible for extracting the raw dataset of US Natural Disaster Declarations from the FEMA API and saving it as a CSV file for further analysis and visualization.
import pandas as pd

# Function to fetch the dataset from the FEMA API and return it as a pandas DataFrame
def get_summaries_dataframe():
    url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv"
    df = pd.read_csv(url, low_memory=False)
    return df

# Function to save the DataFrame to a CSV file
def save_dataframe_to_csv(df, filename):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    df = get_summaries_dataframe()
    print("Dataset Shape:", df.shape)
    print(df.head())

    save_dataframe_to_csv(
        df,
        r"D:\My Project\Visualizing US Natural Disaster Declarations\Data\raw\disaster_declarations_summaries.csv"
    )

    print("Raw dataset saved successfully.")
