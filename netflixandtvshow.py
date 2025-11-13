import pandas as pd

# 1️⃣ Load the dataset
df = pd.read_csv("netflix_titles.csv")

# 2️⃣ Identify missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# 3️⃣ Handle missing values
df.fillna({
    'director': 'Unknown',
    'cast': 'Not available',
    'country': 'Unknown',
    'rating': df['rating'].mode()[0],
    'duration': '0 min',
    'date_added': 'Unknown'
}, inplace=True)

# 4️⃣ Remove duplicate rows
df.drop_duplicates(inplace=True)

# 5️⃣ Standardize text values (example)
# Convert text columns to lowercase and strip spaces
text_columns = ['type', 'country', 'rating']
for col in text_columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

# Example: Standardize country names
df['country'] = df['country'].replace({
    'united states': 'usa',
    'united kingdom': 'uk',
    'south korea': 'korea'
})



# Convert and clean 'date_added'
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')
df['date_added'] = df['date_added'].fillna('Unknown')


# 7️⃣ Rename columns to be uniform (lowercase, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 8️⃣ Check and fix data types
# Example: ensure release_year is int
df['release_year'] = df['release_year'].astype(int)

# 9️⃣ Save cleaned dataset
df.to_csv("fully_cleaned_netflix_titles.csv", index=False)

print("\n✅ Data cleaning complete! Saved as 'fully_cleaned_netflix_titles.csv'")
print("\nMissing values after cleaning:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)