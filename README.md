# Netflix-and-TV-shows-Data_Cleaning_Task1
"Data cleaning and Preprocessing Internship Task
Data Cleaning and Preprocessing – Task 1

Internship: Data Analyst Intern
Objective: Clean and preprocess a raw dataset from Kaggle to make it ready for analysis.
Tool used:Python (Pandas)

📂 Dataset Used

Name: Netflix Movies and TV Shows Dataset
Source: Kaggle - Netflix Movies and TV Shows

⚙️ Steps Performed

1️⃣ Load the Dataset
   
    df = pd.read_csv("netflix_titles.csv")

Imported the Netflix dataset into a Pandas DataFrame for processing.

2️⃣ Identify Missing Values
   
    df.isnull().sum()

*Checked for missing data across all columns.
*Identified nulls in columns such as director, cast, country, rating, duration, and date_added.

3️⃣ Handle Missing Values

    df.fillna({
    'director': 'Unknown',
    'cast': 'Not available',
    'country': 'Unknown',
    'rating': df['rating'].mode()[0],
    'duration': '0 min',
    'date_added': 'Unknown'
    }, inplace=True)

*Replaced null values with appropriate placeholders or statistical replacements:
*Text fields like director and cast were replaced with "Unknown" or "Not available".
*rating column filled with the most frequent value (mode).
*duration filled with "0 min".
*date_added set to "Unknown" if missing.

4️⃣ Remove Duplicate Records
    
    df.drop_duplicates(inplace=True)

*Removed all duplicate rows to ensure data integrity.

5️⃣ Standardize Text Values
    
    text_columns = ['type', 'country', 'rating']
    for col in text_columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

*Converted key text columns to lowercase and removed extra spaces.
*Standardized specific country names for consistency:
  
    df['country'] = df['country'].replace({
    'united states': 'usa',
    'united kingdom': 'uk',
    'south korea': 'korea'
   })

6️⃣ Format Dates
   
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')
    df['date_added'] = df['date_added'].fillna('Unknown')

*Converted date_added to a proper date format (DD-MM-YYYY).
*Handled invalid or missing dates gracefully by replacing them with "Unknown".

7️⃣ Ensure Correct Data Types
   
    df['release_year'] = df['release_year'].astype(int)

*Confirmed that release_year column contains integer values.

8️⃣ Save the Cleaned Dataset
   
    df.to_csv("fully_cleaned_netflix_titles.csv", index=False)

*Exported the cleaned data into a new CSV file named fully_cleaned_netflix_titles.csv.
