import network
from fastapi import FastAPI

api_test = FastAPI()
hosts_tests = network.status_hosts()

@api_test.get("/status-host")
def get_status_hosts():
    pass