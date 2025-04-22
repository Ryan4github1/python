import datetime
from datetime import date,time
import pytz
ist = pytz.timezone('Asia/kolkata')
print(" ist in default format : ",datetime.datetime.now(ist))
ast=pytz.timezone('Australia/sydney')
print("AEST in default format : ",datetime.datetime.now(ast))