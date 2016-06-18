import os

KEY = os.urandom(24).encode('base-64').rstrip('\n')
