import os
from datetime import datetime
import mysql.connector

def return_basic(request):
  now = datetime.now()
  return '<h1>test function</h1><br/>' + str(now)
