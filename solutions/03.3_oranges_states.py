oranges = gdf.loc[gdf['COMMODITY_DESC'] == 'Oranges', ['COMMODITY_DESC', 'STATE_NAME']]

oranges['STATE_NAME'].unique()