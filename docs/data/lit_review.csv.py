# import pandas as pd
# from pathlib import Path
# import sys

import csv
from pathlib import Path
import sys

# List of CSV file paths
fnames = list(Path("docs/data/lit_reviews").glob("*csv"))

# Create a list to store the combined data
combined_data = []

# Iterate through each file
for f in fnames:
    source = f.stem  # Get the file name without extension
    with f.open('r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['source'] = source  # Add the source column
            combined_data.append(row)

# Get the fieldnames (columns) from the first row
fieldnames = combined_data[0].keys()

# Write the combined data to stdout
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
writer.writeheader()
for row in combined_data:
    writer.writerow(row)
