print(gdf.dtypes)

gdf['STATE_ANSI'] = gdf['STATE_ANSI'].astype('int32')
gdf['ASD_CODE'] = gdf['ASD_CODE'].astype('int32')