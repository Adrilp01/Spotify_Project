The goal of this project was to visualize and analyze my personal Spotify listening history. To do this, I followed several steps: 

1-	I requested my data from Spotify, and they sent me four different JSON files, each corresponding to a year of listening history.

2-	I then created a Python script to convert those JSON files into a single CSV file for use in Power BI. In the script, I looped through the four JSONs, loaded them as dataframes, added them to a list, and then concatenated them all. After that, I exported the final dataframe as a CSV.

3-	In Power BI, I cleaned and prepared the data. For example, some columns like the IP address weren’t in the correct data type, so I fixed those issues. I also made some adjustments, such as creating a custom column to identify the brand of the devices I used.
