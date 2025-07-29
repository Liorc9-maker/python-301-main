# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.
# type: ignore
import usr_pass
import sqlalchemy
from pprint import pprint

# Create the engine with f-string to inject variables
try:
    engine = sqlalchemy.create_engine(
        f"mysql+pymysql://{usr_pass.username}:{usr_pass.password}@localhost/sakila"
    )
    connection = engine.connect()
except Exception as e:
    print("Failed to connect to the database.")
    print("Error:", e)
else:
    print("Connection successful. Fetching data...")

    metadata = sqlalchemy.MetaData()
    actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)

    query = sqlalchemy.select(actor)
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()

    pprint(result_set)

    connection.close()
