from utils import query_duckdb

query_duckdb("""
    CREATE TABLE IF NOT EXISTS movies (
             title STRING,
             year INTEGER,
             genre STRING,
             rating FLOAT
    );
""")

if __name__ == "__main__":
    print(query_duckdb("DESC;"))