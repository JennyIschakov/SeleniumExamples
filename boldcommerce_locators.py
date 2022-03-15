import random

from faker import Faker


# =================================================== Variables
fake = Faker('en_CA')


# URLs
home_page_url = 'https://boldcommerce.com/'

# Random fake variables for form
first_name = fake.first_name()
last_name = fake.last_name()

domain_list = ['gmail.com', 'yahoo.com']
email = f'{first_name}.{last_name}@{random.choice(domain_list)}'

phone = fake.phone_number()

company_name = fake.sentence(nb_words=1).replace(".", "")
url_ends = ['.com', '.ca']
company_web = f'{company_name}{random.choice(url_ends)}'
