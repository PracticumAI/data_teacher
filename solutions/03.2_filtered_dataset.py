df_filtered = df_subset[(df_subset['price']>=50) & (df_subset['price']<=100)]
answer = df_filtered.shape[0]

print(f"There are {answer} rows of the wine price are between $50 and $100")