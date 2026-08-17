import os 
secret = os.environ.get ("DB_PASSWORD")
print(f"Python retrieved secret password from Linux Memory : {secret}")

