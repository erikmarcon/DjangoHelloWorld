import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

database = psycopg2.connect(
    host = 'localhost',
    user = 'erikbrm',
    password = '',
    port = 5432
    )

database.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Prepare Cursor Object
cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE helloworld')

print('All Done!')