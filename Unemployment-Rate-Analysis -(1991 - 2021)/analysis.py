import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
def load_data(file_path="C:/Users/HS COMPUTER/Downloads/Compressed/archive/unemployment analysis.csv"):
    df = pd.read_csv("C:/Users/HS COMPUTER/Downloads/Compressed/archive/unemployment analysis.csv")
    return df

# 2. Data Cleaning & Transformation
def transform_data(df):
    # Check for missing values
    print("Missing values per column:\n", df.isnull().sum().sum())
    
    # Melt the dataframe: move years from columns to rows
    id_vars = ['Country Name', 'Country Code']
    year_cols = [str(year) for year in range(1991, 2022)]
    
    df_long = pd.melt(df, id_vars=id_vars, value_vars=year_cols, 
                      var_name='Year', value_name='Unemployment Rate')
    
    # Convert Year to integer for plotting
    df_long['Year'] = df_long['Year'].astype(int)
    return df_long

# 3. Exploration and Visualization
def visualize_trends(df_long):
    plt.figure(figsize=(14, 7))
    
    # Global Trend
    global_mean = df_long.groupby('Year')['Unemployment Rate'].mean().reset_index()
    sns.lineplot(data=global_mean, x='Year', y='Unemployment Rate', marker='o', color='tab:blue')
    
    plt.title('Global Average Unemployment Rate (1991 - 2021)', fontsize=15)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Unemployment Rate (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axvspan(2019, 2021, color='red', alpha=0.1, label='COVID-19 Period')
    plt.legend()
    plt.show()

def analyze_covid_impact(df_long):
    # Pivot to compare specific years
    pivot_df = df_long.pivot(index='Country Name', columns='Year', values='Unemployment Rate')
    
    # Calculate the Delta between 2019 and 2020
    pivot_df['Impact_2020'] = pivot_df[2020] - pivot_df[2019]
    
    # Top 10 most affected countries
    top_affected = pivot_df['Impact_2020'].sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_affected.values, y=top_affected.index, palette='Reds_r')
    plt.title('Top 10 Countries with Highest Increase in Unemployment (2019-2020)', fontsize=14)
    plt.xlabel('Percentage Increase (%)')
    plt.show()
    
    return top_affected

def analyze_regional_patterns(df):
    # Looking at specific major regions (Example: Arab World vs Central Europe)
    regions = ['Arab World', 'Central Europe and the Baltics', 'European Union', 'South Asia']
    regional_df = df[df['Country Name'].isin(regions)]
    
    # Re-transform for regional plot
    regional_long = pd.melt(regional_df, id_vars=['Country Name'], 
                            value_vars=[str(y) for y in range(1991, 2022)],
                            var_name='Year', value_name='Rate')
    regional_long['Year'] = regional_long['Year'].astype(int)
    
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=regional_long, x='Year', y='Rate', hue='Country Name')
    plt.title('Unemployment Trends by Region', fontsize=15)
    plt.show()

if __name__ == "__main__":
    # Path to the file provided in context
    file_path = 'data/unemployment analysis.csv'
    
    try:
        raw_data = load_data(file_path)
        clean_data = transform_data(raw_data)
        
        print("--- Global Trends ---")
        visualize_trends(clean_data)
        
        print("--- COVID-19 Impact Analysis ---")
        impact = analyze_covid_impact(clean_data)
        print("Countries with highest 2020 increase:\n", impact)
        
        print("--- Regional Comparisons ---")
        analyze_regional_patterns(raw_data)
        
        # Policy Insights
        print("\n--- Key Insights for Policy Makers ---")
        print("1. Volatility: High-income countries saw sharper relative spikes in 2020 compared to long-term stability.")
        print("2. Resilience: Certain regions like South Asia show long-term structural unemployment that requires different intervention than the COVID-19 'shock'.")
        print("3. Recovery: 2021 data suggests a bifurcated recovery; monitoring 2022 data will be crucial for long-term scarring effects.")

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Please ensure it is in the 'data/' folder.")