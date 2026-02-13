# converts the data to the dataframe
import pandas as pd
import requests


def get_summaries_dataframe():
    url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
    response = requests.get(url)
    data = response.json()
    summaries = data["DisasterDeclarationsSummaries"]
    df = pd.DataFrame(summaries)
    return df
if __name__ == "__main__":
    df = get_summaries_dataframe()
    print(df.head())

# stores the dataframe in a csv file
def save_dataframe_to_csv(df, filename):
    df.to_csv(filename, index=False)
if __name__ == "__main__":
    df = get_summaries_dataframe()
    save_dataframe_to_csv(df, r"D:\My Project\Visualizing US Natural Disaster Declarations\Data\raw\disaster_declarations_summaries.csv")

