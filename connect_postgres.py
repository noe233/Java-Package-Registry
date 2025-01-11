import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "postgres"  # Replace with your database name
DB_USER = "dany"  # Replace with your username
DB_PASSWORD = "123"  # Replace with your password

def create_find_central_repo():
        # Create central 
    cursor.execute(
                    "SELECT * FROM MavenRepository WHERE name = %s", 
                    ('central',)
                )
    result = cursor.fetchone()
                
    if result:
        print("Central repository already exists:", result)
    else:
        # Insert the 'central' repository if it doesn't exist
        cursor.execute(
                 """
                INSERT INTO MavenRepository (name, url, lastRefreshed, state, stateMsg)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """,
                ('central', 'https://repo1.maven.org/maven2/', None, 0, None)
                )
        central_id = cursor.fetchone()[0]
        connection.commit()
        print(f"Central repository created with ID: {central_id}")



try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("Connection to the database established successfully!")
    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    create_find_central_repo()

    
except Exception as e:
    print(f"An error occurred: {e}")
    raise e

finally:
    # Close the connection
    if 'connection' in locals() and connection:
        connection.close()
        print("Database connection closed.")    
    
    
    """# Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example query: Create a simple table
    cursor.execute(
        sql.SQL(\"""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
        \""")
    )
    connection.commit()
    print("Table created successfully!")

    # Insert a sample record
    cursor.execute(
        sql.SQL("INSERT INTO test_table (name) VALUES (%s);"),
        ("Sample Name",)
    )
    connection.commit()
    print("Record inserted successfully!")

    # Fetch and print records
    cursor.execute(sql.SQL("SELECT * FROM test_table;"))
    rows = cursor.fetchall()
    for row in rows:
        print(row)"""


