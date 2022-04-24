import sqlite3

conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("db/users.db")

# Create a cursor, the thing we create to do the things.
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE users2 (
    name TEXT,
    game TEXT,
    email TEXT
)""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Commit our commans
conn.commit()

# Close our connection
conn.close()

