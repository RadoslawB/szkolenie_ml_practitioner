import pandas as pd
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta

def import_tips_dataset():
    df = sns.load_dataset('tips')
    
    day_map = {
        'Thur': '2026-03-26',
        'Fri':  '2026-03-27',
        'Sat':  '2026-03-28',
        'Sun':  '2026-03-29'
    }
    
    time_map = {
        'Lunch': 13,
        'Dinner': 19
    }
    
    np.random.seed(42)
    
    def generate_timestamp(row):
        base_date = day_map[row['day']]
        base_hour = time_map[row['time']]
        random_minutes = np.random.randint(0, 180)
        
        ts = datetime.strptime(f"{base_date} {base_hour}:00", "%Y-%m-%d %H:%M")
        ts += timedelta(minutes=random_minutes)
        return ts

    df['order_at'] = df.apply(generate_timestamp, axis=1)
    
    # Usuwamy kolumnę 'day' zgodnie z prośbą
    df = df.drop(columns=['day'])
    
    df = df.sort_values('order_at').reset_index(drop=True)
    
    return df
