from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
import requests
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",format="%(asctime)s %(levelname)s %(message)s")




urls = range(1,10)
un=['9819263292','7411132994']
pwd=['123456','123456']
time_as_list=[]

def get_data(un,pwd,urls):
    logging.info("---------- \n")
    myobj={'username':un,'password':pwd}
    start = perf_counter()
    r = requests.post(f'https://learn.artiumacademy.com/api/auth/login',json=myobj)
    stop = perf_counter()
    timeTaken=stop - start
    logging.info(f"time taken:{stop - start}")
    time_as_list.append(timeTaken)
    logging.info("---------- \n ")
    logging.info(f"Response is:{r.json()}")
    logging.info("---------- \n ")

with ThreadPoolExecutor() as executor:
    executor.map(get_data,un,pwd ,urls)

print(time_as_list)