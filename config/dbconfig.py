import os
from urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

pg_config = {
    'user' : user,
    'passwd' : password,
    'dbname' : dbname
}
##appusr
##appusr1
##appdb
