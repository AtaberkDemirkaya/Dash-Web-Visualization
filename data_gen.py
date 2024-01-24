import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate example data
np.random.seed(42)
timestamps = pd.date_range(datetime.now() - timedelta(days=30), datetime.now(), freq='D')
data = {
    'TIMESTAMP': timestamps,
    'ALARM_NAME': np.random.choice(['ACTIVE SESSION', 'HIGH CPU USAGE', 'LOW MEMORY'], len(timestamps)),
    'DATABASE_NAME': np.random.choice(['DB_1', 'DB_2', 'DB_3'], len(timestamps)),
    'VALUE': np.random.rand(len(timestamps)) * 100,
    'WARNING': np.full(len(timestamps), 30),  # Constant WARNING value
    'CRITICAL': np.full(len(timestamps), 60)  # Constant CRITICAL value (higher than WARNING)
}

df = pd.DataFrame(data)

# Save to Excel file
df.to_excel("data.xlsx", index=False)
