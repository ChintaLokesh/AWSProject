from logging.handlers import RotatingFileHandler
import logging
from time import perf_counter
import requests
from concurrent.futures import ThreadPoolExecutor


logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("py_log.log", maxBytes=20_971_520,
                                  backupCount=10)
logger.addHandler(handler)

urls = range(1,10)
time_as_list=[]
time_as_dict={}


def getRefreshToken(un:str,pwd:str):
    myobj={'username':un,'password':pwd}
    r = requests.post(f'https://learn.artiumacademy.com/api/auth/login',json=myobj)
    # json_response=r.json()
    logger.info(f" Authorization is: {r.headers['Authorization']}")
    return(r.headers['Authorization'])

def get_data(un,pwd,urls):
    un="7001899642"
    pwd="743252"
    Authorization=getRefreshToken(un,pwd)
    
   
    # logger.info(f"refresh token is {Authorization}")
    headers = {
    'Authorization': 'Bearer '+Authorization,
    }
    params = {
    'fromDate': '2023-06-01',
    'toDate': '2023-06-14',
    'teacherId':325
    }
    start = perf_counter()
    r = requests.get(f'https://beta.artiumacademy.com:8765/api/course/teacherpayoutprice', headers=headers,params=params)
    stop = perf_counter()
    timeTaken=stop - start
    logger.info(f"time taken:{timeTaken} seconds ")
    logger.info(f"payout api response code is {r.status_code}")
    logger.info(f"payout api response code is {r.json()}")
    time_as_dict={'urls':'timeTaken'}
    time_as_list.append(timeTaken)
    logger.info("---------- \n ")

    # logger.info(f"Response is:{r.json()}")

    logger.info("---------- \n ")

with ThreadPoolExecutor() as executor:
    # executor.map(get_data("9819263292","123456",urls))
    un="7001899642"
    pwd="743252"
    executor.map(get_data,un,pwd,urls)


print((time_as_list))
print(f" maximum time taken to load the api is {max(time_as_list)}")