import pandas as pd
import sqlite3

from pathlib import Path

parent = Path(Path.cwd()).parent
connection = sqlite3.connect(f"{parent}/backends/database.db")

crsr = connection.cursor()

crsr.execute("""
    SELECT * FROM user
""")

df = pd.DataFrame(crsr.fetchall())
df.style
