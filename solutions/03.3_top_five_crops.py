state_groups = gdf[['STATE_NAME', 'COMMODITY_DESC']].groupby(['STATE_NAME'])

florida = state_groups.get_group('FLORIDA')

florida.value_counts()[:5]