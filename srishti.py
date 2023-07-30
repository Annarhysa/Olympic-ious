import pandas as pd
def retrieve_summary(dataset,keyword):
  keyword= keyword.lower()
  filtered_data= dataset[dataset['country_name'].str.contains(keyword, case = False)]
  summaries= filtered_data['summary'].tolist()
  return summaries
if __name__ == "__main__":
  dataset= pd.read_csv('D:\Olympics_summary.csv')
  keyword_to_retrieve = input("Enter Country:")
  keyword_summaries = retrieve_summary(dataset,keyword_to_retrieve)
  if keyword_summaries:
    for idx,summary in enumerate(keyword_summaries,1):
      print(f"{summary}")
  else:
    print("Country Unavailable")