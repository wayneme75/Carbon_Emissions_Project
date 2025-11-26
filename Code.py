from operator import index
import pandas as pd 
#Show all columns and rows when printing dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
excel_path="National_Fossil_Carbon_Emissions_2025_v0.3.xlsx"
df=pd.read_excel(excel_path, engine="openpyxl")
#Gathering stats on the data set
print(df.head())
print(df.columns)
print(df.head(20))
print("Number of NaN values in each column:")
print(df.isnull().sum())
#Cleaning the data set by removing rows with NaN values
df_cleaned=df.dropna()
print("Number of NaN values in each column after cleaning:")
print(df_cleaned.isnull().sum())
print(df_cleaned.head())
print(df_cleaned.dtypes)
#convert data types from object to numeric for analysis
df_cleaned=df_cleaned.apply(pd.to_numeric, errors='ignore')
print(df_cleaned.dtypes)
#Look at stats after converting data types
print(df_cleaned.describe())
#Drop first column Unnamed:0
df_cleaned=df_cleaned.drop(columns=['Unnamed: 0'])
#Calculate the country with the highest average fossil carbon emissions
highest_avg_emissions=df_cleaned.mean().idxmax()
#print("The country with the highest average fossil carbon emissions is:", highest_avg_emissions)
if highest_avg_emissions == "World":
    print("The world's output is:", highest_avg_emissions)
else:
    print("The country with the highest average fossil carbon emissions is:", highest_avg_emissions)
#Drop the column titled world 
df_cleaned=df_cleaned.drop(columns=['World'])
#Calculate the country with the highest average fossil carbon emissions after dropping world column
highest_avg_emissions=df_cleaned.mean().idxmax()
print("The country with the highest average fossil carbon emissions after dropping World column is:", highest_avg_emissions)
#Print the value of the mean of Non-OECD
print("The value of the mean for Non-OECD:", df_cleaned['Non-OECD'].mean())
#Drop statistical diffefence columns
df_cleaned=df_cleaned.drop(columns=['Statistical Difference'])
#Calculate the country with the lowest average fossil carbon emissions
lowest_avg_emissions=df_cleaned.mean().idxmin()
print("The country with the lowest average fossil carbon emissions is:", lowest_avg_emissions)
#Print the value of the mean of NIUE
print("The value of the mean for NIUE:", df_cleaned['NIUE'].mean())
#Remove all grouped countries to analyze only individual countries
grouped_countries=['KP Annex B', 'Non KP Annex B', 'OECD', 'Non-OECD', 'EU27', 'Africa', 'Asia', 'Central America', 'Europe', 'Middle East', 'North America', 'Oceania', 'South America', 'International Shipping', 'International Aviation']
df_individual_countries=df_cleaned.drop(columns=grouped_countries)
#Calculate the country with the highest average fossil carbon emissions among individual countries
highest_avg_emissions_individual=df_individual_countries.mean().idxmax()
print("The individual country with the highest average fossil carbon emissions is:", highest_avg_emissions_individual)
print("The value of the mean for", highest_avg_emissions_individual, "is:", df_individual_countries[highest_avg_emissions_individual].mean())
#Calculate the country with the lowest average fossil carbon emissions among individual countries
lowest_avg_emissions_individual=df_individual_countries.mean().idxmin()
print("The individual country with the lowest average fossil carbon emissions is:", lowest_avg_emissions_individual)
print("The value of the mean for", lowest_avg_emissions_individual, "is:", df_individual_countries[lowest_avg_emissions_individual].mean())
#Calculate the top 5 countries in order with the highest average fossil carbon emissions in order
top_5_countries= df_individual_countries.mean(axis=0).sort_values(ascending=False).head(5).index.tolist()
print("The top 5 individual countries in orderwith the highest average fossil carbon emissions are:", top_5_countries)
#Calculate the bottom 5 countries from lowest to highest with the lowest average fossil carbon emissions
bottom_5_countries= df_individual_countries.mean(axis=0).sort_values(ascending=True).head(5).index.tolist()
print("The bottom 5 individual countries from least to most with the lowest average fossil carbon emissions are:", bottom_5_countries)
#Calculate the standard deviation of fossil carbon emissions for the top 5 countries
std_dev_top_5={}
for country in top_5_countries:
    std_dev_top_5[country]=df_individual_countries[country].std()
print("The standard deviation of fossil carbon emissions for the top 5 countries are:", std_dev_top_5)
#Calculate the standard deviation of fossil carbon emissions for the bottom 5 countries
std_dev_bottom_5={}
for country in bottom_5_countries:
    std_dev_bottom_5[country]=df_individual_countries[country].std()
print("The standard deviation of fossil carbon emissions for the bottom 5 countries are:", std_dev_bottom_5)