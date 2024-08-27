import atexit
from time import sleep

@atexit.register
def final_function():
    print("EXÉCUTION TERMINÉE !")
    
for i in range(5):
    print(f"num = {i}")