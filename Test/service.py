#Business logic goes in this file. You can remane this file as per your understanding or requirement
from .models import Test

def get_all_tests():
    try:
        test = Test.query.limit(1).all() #Get all data from Test table
        print(test)
    except Exception as e:
        print(e)
        #handle and send proper response to controller