grouped_by_country = df_subset.groupby('country')
summary_statistics = grouped_by_country['price'].describe()
us_avg_price = summary_statistics.loc['US', 'mean']
print(f"The average wine price in the US is {us_avg_price:.2f} dollars.")