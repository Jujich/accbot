from sqlalchemy import create_engine
from dotenv import load_dotenv
if __name__ == '__main__':
    load_dotenv()
import os

pgpassword = os.environ.get('PG_PASSWORD')
pgip = os.environ.get('PG_PASSWORD')

engine = create_engine(f'postgresql://postgres:{pgpassword}@{pgip}:5432/accbot')
