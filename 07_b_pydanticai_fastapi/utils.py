from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data"

def query_duckdb(sql_code: str, parameters = None):
    with duckdb.connect(DATA_PATH / "movies.db") as conn:
        cursor = conn.execute(sql_code, parameters=parameters)

        if (
            sql_code.strip()
            .lower()
            .startswith(("select", "with", "from", "desc", "pragma"))
        ):
            return cursor.df()