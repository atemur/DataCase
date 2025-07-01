from datetime import datetime, timedelta, timezone

TURKEY_TZ = timezone(timedelta(hours=3))
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S+03:00"
start_date = (datetime.now(TURKEY_TZ) - timedelta(days=30)).strftime(DATE_FORMAT)
end_date = datetime.now(TURKEY_TZ).strftime(DATE_FORMAT)
end_date_for_c1 = (datetime.now(TURKEY_TZ) - timedelta(days=1)).strftime(DATE_FORMAT)

BASE_URL = "https://seffaflik.epias.com.tr/electricity-service/v1"
TOKEN =  "https://giris.epias.com.tr/cas/v1/tickets"

ENDPOINTS = {
    "POWER_PLANTS": "/markets/data/power-plant-list-by-organization-id",
    "UEVCB_LIST": "/markets/data/uevcb-list-by-power-plant-id",
    "REALTIME_PLANTS": "/generation/data/powerplant-list",
    "DAM_CLEARING": "/markets/dam/data/clearing-quantity",
    "IDM_MATCHING": "/markets/idm/data/matching-quantity",
    "BILATERAL_BID": "/markets/bilateral-contracts/data/bilateral-contracts-bid-quantity",
    "BILATERAL_OFFER": "/markets/bilateral-contracts/data/bilateral-contracts-offer-quantity",
    "REALTIME_GEN": "/generation/data/realtime-generation",
    "DPP": "/generation/data/dpp",
}

USERNAME = "your_email@gmail.com"
PASSWORD = "your_password"

REGION = "TR1"

organizationIDs = [0000, 0000, 0000, 0000, 0000]
