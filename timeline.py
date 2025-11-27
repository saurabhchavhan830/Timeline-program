# Create a simple timeline program 

from datetime import datetime

today = datetime.now()

christamas = datetime(2025,12,25)

days_laft = (christamas - today).days

print(f"Days Until for Christamas : {days_laft}")