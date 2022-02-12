from faker import Faker

homepage_url = 'https://www.opencart.com/'
homepage_title = 'OpenCart - Open Source Shopping Cart Solution'

fake = Faker(locale='en_Ca')
new_username = fake.user_name()
new_firstname = fake.first_name()
new_lastname = fake.last_name()
new_email = fake.email()
new_password = fake.password()

items_list = ['Form Builder', 'AJAX Quick Checkout PRO', 'Pro Email Template',
              'Facebook for OpenCart', 'PayPal Commerce Platform' ]


#  ----------------------------------------------------------------

captcha_list = [
    'Light Bulb',
    'Fire',
    'House',
    'Printer',
    'Balloons',
    'Airplane',
    'Umbrella',
    'Scissors',
    'Clock',
    'Sunglasses',
    'Pencil',
    'Music Note',
    'T-Shirt',
    'Camera',
    'Cat',
    'Graph',
    'Puzzle',
    'Dialog',
    'Star',
    'Key',
    'Tree',
    'Foot',
    'Pants',
    'ShoppingCart',
    'Car',
    'Envelope',
    'Lock',
    'PaperPlane',
    'Eye',
    'Woman',
    'World',
    'Chair',
    'OpenCart',
    'Man',
    'Robot',
    'Airplane'
]

captcha_image = [
    '+qHZUUs5CqB',  # Light Bulb
    '+qa+d/2jfGG',  # Fire
    '+qHZURmdgqq',  # House
    '+qa+f/j/AON',  # Printer
    '94+LHi5/Bfg',  # Balloons
    '998aeP8ARPB',  # Airplane
    '+lPFHiDTfC+',  # Umbrella
    '9n+O97rGmfD',  # Scissors
    '7T4/eL/Fdnr',  # Clock
    '+qaK8B+L3xQ',  # Sunglasses
    '+qaKDXjvxs+',  # Pencil
    '+qa4v4xa/qP',  # Music Note
    '+k/EviLSPDG',  # T-Shirt
    '+j9d8U6HoF3',  # Camera
    '+qaKK+afip8',  # Cat
    '9r8IeOrvXfi',  # Graph
    '+qaYZoh1kT/',  # Puzzle
    '+lfEuv6Z4a0',  # Dialog
    '+qa5X4n+KV8',  # Star
    '+qa+bfiV8Vd',  # Key
    '+jvFvirR/Ce',  # Tree
    '+qa5vxD4st9',  # Foot
    '9/8Ainrt54a',  # Pants
    '9O8X/GC88Na',  # ShoppingCart
    '+qaK808Y/Gr',  # Car
    '968SfEnwh4a',  # Envelope
    '+qScDJ6V5IP',  # Lock
    '+qabLIkMZeV',  # PaperPlane
    '+qazNV8QaNp',  # Eye
    '+qa8z+POo+I',  # Woman
    '+gPiF4zsvBe',  # World
    '+qa8W/aN8S+',  # Chair
    '+nrLUbW9uLu',  # OpenCart
    '+qa86+Ner6t',  # Man
    '+qa8D+OPibU',  # Robot
    '998aeP8ARPB'   # Airplane
]