import requests, logging, time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)

# 该网站每隔5秒相应一次
URL = "https://www.httpbin.org/delay/5"

TOTAL_NUMBER = 100
start_time = time.time()
for _ in range(1, TOTAL_NUMBER + 1):
    logging.info("scraping %s", URL)
    response = requests.get(URL)
end_time = time.time()
logging.info("total time %s seconds", end_time - start_time)
