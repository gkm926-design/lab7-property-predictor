import pandas as pd

# The specific columns recommended in your lab instructions
columns_to_keep = [
    "APPRAISED_VALUE", "LAND_VALUE", "BUILD_VALUE", "YARDITEMS_VALUE", "CALC_ACRES",
    "ZONING_DESC", "NEIGHBORHOOD_CODE_DESC", "LAND_USE_CODE_DESC", "PROPERTY_TYPE_CODE_DESC"
]

print("Loading the giant Excel file... (this might take a minute)")
# Read only the necessary columns from the Excel file
df = pd.read_excel("Housing_Hamilton_County.xlsx", usecols=columns_to_keep)

print("Applying lab cleaning steps to shrink size further...")
# Drop rows with missing or invalid APPRAISED_VALUE as required by the lab
df = df.dropna(subset=["APPRAISED_VALUE"])
df = df[df["APPRAISED_VALUE"] > 0]

print("Compressing and saving...")
# Save it as a highly compressed GZIP CSV
df.to_csv("Housing_Hamilton_Compressed.csv.gz", compression="gzip", index=False)

print("Done! The file is now compressed and ready for GitHub.")
