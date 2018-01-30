import os
from urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
# url = parse.urlparse(os.environ["DATABASE_URL"])
url = parse.urlparse("postgresql://appusr:appusr1@hurricanerelief.cybd6a6s6wh4.us-east-1.rds.amazonaws.com/appdb")
##appusr
##appusr1
##appdb
