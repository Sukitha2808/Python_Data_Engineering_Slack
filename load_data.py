# load_data.py
import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import quote_plus

# --- Load .env automatically from script folder ---
dotenv_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

# --- Helper function to parse dates ---
def parse_date(date_str):
    if pd.isna(date_str) or date_str in ('', 'NULL'):
        return None
    try:
        return datetime.strptime(str(date_str), '%m/%d/%Y').date()
    except ValueError:
        try:
            return pd.to_datetime(date_str, errors='coerce').date()
        except:
            return None

# --- Main function ---
def load_data():
    # Load database credentials from environment
    db_user = os.getenv('DB_USER', 'root')
    db_password = quote_plus(os.getenv('DB_PASSWORD', 'Suki@2808'))
    db_host = os.getenv('DB_HOST', 'localhost')
    db_name = os.getenv('DB_NAME', 'supply_chain')
    db_port = os.getenv('DB_PORT', '3306')

    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(f"Connecting to: {connection_string.replace(db_password, '********')}")

    try:
        engine = create_engine(connection_string)
        
        # Test connection
        with engine.connect() as conn:
            print("Connected to MySQL database successfully!")
        
        # --- Detect CSV files in the same folder as script ---
        script_folder = Path(__file__).parent
        csv_files = {
            'vendors': script_folder / 'vendors.csv',
            'inventory': script_folder / 'inventory (1).csv',
            'shipments': script_folder / 'shipments.csv',
            'delivery_logs': script_folder / 'delivery_logs.csv',
            'claims': script_folder / 'claims.csv'
        }

        # Load CSVs
        dataframes = {}
        for name, path in csv_files.items():
            if not path.exists():
                raise FileNotFoundError(f"{path} not found")
            df = pd.read_csv(path)
            dataframes[name] = df
            print(f"Loaded {name}: {len(df)} records")

        # --- Data cleaning & transformations ---
        # Vendors
        vendors_df = dataframes['vendors']
        for col in ['contract_start', 'contract_end']:
            if col in vendors_df.columns:
                vendors_df[col] = vendors_df[col].apply(parse_date)
        if 'vendor_rating' in vendors_df.columns:
            vendors_df['vendor_rating'] = pd.to_numeric(vendors_df['vendor_rating'], errors='coerce')

        # Inventory
        inventory_df = dataframes['inventory']
        for col in ['last_restock_date', 'next_restock_due']:
            if col in inventory_df.columns:
                inventory_df[col] = inventory_df[col].apply(parse_date)
        for col in ['stock_level', 'reorder_threshold']:
            if col in inventory_df.columns:
                inventory_df[col] = pd.to_numeric(inventory_df[col], errors='coerce').fillna(0).astype(int)

        # Shipments
        shipments_df = dataframes['shipments']
        for col in ['ship_date', 'delivery_date']:
            if col in shipments_df.columns:
                shipments_df[col] = shipments_df[col].apply(parse_date)
        for col in ['quantity', 'freight_cost']:
            if col in shipments_df.columns:
                shipments_df[col] = pd.to_numeric(shipments_df[col], errors='coerce').fillna(0)

        # Delivery logs
        delivery_logs_df = dataframes['delivery_logs']
        if 'delivery_duration_days' in delivery_logs_df.columns:
            delivery_logs_df['delivery_duration_days'] = pd.to_numeric(delivery_logs_df['delivery_duration_days'], errors='coerce').fillna(0).astype(int)
        if 'damage_flag' in delivery_logs_df.columns:
            delivery_logs_df['damage_flag'] = delivery_logs_df['damage_flag'].astype(str).str.lower().map({
                'true': True, '1': True, 'yes': True, 'y': True,
                'false': False, '0': False, 'no': False, 'n': False
            }).fillna(False)

        # Claims
        claims_df = dataframes['claims']
        for col in ['claim_date', 'resolved_date']:
            if col in claims_df.columns:
                claims_df[col] = claims_df[col].apply(parse_date)
        if 'amount_claimed' in claims_df.columns:
            claims_df['amount_claimed'] = pd.to_numeric(claims_df['amount_claimed'], errors='coerce').fillna(0.0)

        # --- Load data into MySQL in correct order ---
        print("Loading data into MySQL...")
        shipments_df.to_sql("shipments", con=engine, if_exists="append", index=False, method='multi')
        print("✓ Shipments data loaded")
        vendors_df.to_sql("vendors", con=engine, if_exists="append", index=False, method='multi')
        print("✓ Vendors data loaded")
        inventory_df.to_sql("inventory", con=engine, if_exists="append", index=False, method='multi')
        print("✓ Inventory data loaded")
        delivery_logs_df.to_sql("delivery_logs", con=engine, if_exists="append", index=False, method='multi')
        print("✓ Delivery logs data loaded")
        claims_df.to_sql("claims", con=engine, if_exists="append", index=False, method='multi')
        print("✓ Claims data loaded")

        print("\nAll data loaded successfully!")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()

# --- Run the loader ---
if __name__ == "__main__":
    load_data()
