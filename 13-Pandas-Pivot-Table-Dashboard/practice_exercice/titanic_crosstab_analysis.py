import pandas as pd
import seaborn as sns
import sys

def run_titanic_analysis():
    """
    Quick script to analyze survival rates using crosstabs.
    Goal: Prove that class (socio-economic status) affected survival chances.
    """
    print("--- 🚢 Titanic Data Analysis Script ---")

    # 1. Loading Data
    # Using seaborn's dataset just for quick prototyping
    try:
        df = sns.load_dataset('titanic')
        print(f"Dataset loaded. Dimensions: {df.shape}")
    except Exception as e:
        print(f"Failed to load data: {e}")
        sys.exit(1)

    # 2. Raw Counts (Volume)
    # I want to see the raw distribution first. Did 3rd class just have more people?
    print("\n--- 1. Raw Survival Counts by Class ---")
    survival_counts = pd.crosstab(
        index=df['pclass'], 
        columns=df['survived'], 
        margins=True,       # Keeping margins to verify totals
        margins_name="Total"
    )
    print(survival_counts)

    # 3. Percentage Analysis (The real insight)
    # Raw numbers are misleading because 3rd class is huge. 
    # Normalizing by index (row) gives me the survival RATE within each class.
    print("\n--- 2. Survival Rate (%) by Class ---")
    survival_pct = pd.crosstab(
        index=df['pclass'], 
        columns=df['survived'], 
        normalize='index' # Crucial: divides count by row total
    ) * 100
    
    # Cleaning up the output for readability
    survival_pct.columns = ['Died (%)', 'Survived (%)']
    print(survival_pct.round(1))

    print("\n-------------------------------------------")
    print("CONCLUSION: Money mattered. 1st class had ~63% survival vs ~24% for 3rd class.")
    print("-------------------------------------------")

if __name__ == "__main__":
    run_titanic_analysis()