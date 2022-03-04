import utils
import req

BASE_URL = "http://ip-api.com/json"


SHOW_DATA = {
    "query": "IP",
    "country": "Country",
    "regionName": "Region",
    "city": "City",
    "lat": "Lat",
    "lon": "Lon",
}


def getMyIp():
    data = req.get(BASE_URL, params={"fields": ",".join(SHOW_DATA.keys())})
    for key in SHOW_DATA.keys():
        print(f"{SHOW_DATA[key]}\t: {data[key]}")


def getTheIp():
    ip = input("Enter IP\t: ")
    utils.clearConsole()
    data = req.get(
        f"{BASE_URL}/{ip}", params={"fields": ",".join(SHOW_DATA.keys()), "query": ip}
    )
    for key in SHOW_DATA.keys():
        print(f"{SHOW_DATA[key]}\t: {data[key]}")
