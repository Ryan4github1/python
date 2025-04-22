import datetime
import random
start_date = datetime.date(2023,5,1)
end_date = datetime.date(2024,5,30)
num_days = (end_date - start_date).days
rand_days = random.randint(1, num_days)
random_days = start_date + datetime.timedelta(days=rand_days)
print(random_days)