import pandas as pd

def analyze_mt5_log(csv_file):
    df = pd.read_csv(csv_file)

    # Flag daily equity drawdown breaches (> 5%)
    daily_loss = df.groupby('Date')['Profit'].sum()
    breaches = daily_loss[daily_loss < -500] # Assuming $10k initial equity

    # Detect slippage anomalies (> 3 pips)
    high_slippage = df[df['Slippage_Pips'] > 3.0]

    print("--- DAILY RISK BREACHES ---")
    print(breaches)
    print("\n--- HIGH SLIPPAGE EXECUTION WARNINGS ---")
    print(high_slippage[['TicketID', 'Symbol', 'Slippage_Pips', 'Profit']])

if __name__ == "__main__":
    analyze_mt5_log("mt5_execution_data.csv")
