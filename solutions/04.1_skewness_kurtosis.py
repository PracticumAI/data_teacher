import numpy as np
import pandas as pd
from scipy import stats

# Generate some data with high kurtosis
data = np.random.normal(0, 5, 1000)**3

# Calculate skewness and kurtosis for original data
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# Log transformation
log_data = np.log(data)

# Remove any missing values (NaN) from log_data
log_data = log_data[~np.isnan(log_data)]

# Calculate skewness and kurtosis for log-transformed data
log_skewness = stats.skew(log_data)
log_kurtosis = stats.kurtosis(log_data)

# Display the results
results = pd.DataFrame({
    'Original Data': [skewness, kurtosis],
    'Log Transformed Data': [log_skewness, log_kurtosis]
}, index=['Skewness', 'Kurtosis'])

print(results)