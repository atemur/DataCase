from datetime import datetime, timedelta, timezone

# Türkiye saat dilimi
TURKEY_TZ = timezone(timedelta(hours=3))

# Tarih aralıkları
START_DATE = (datetime.now(TURKEY_TZ) - timedelta(days=30)).isoformat()
END_DATE = datetime.now(TURKEY_TZ).isoformat()

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

# Replace these with your actual credentials
USERNAME = "your_email@example.com"
PASSWORD = "your_password"

ORGANIZATIONS = [
    {"id": 00000, "name": "Organization 1"},
    {"id": 00000, "name": "Organization 2"},
    {"id": 00000, "name": "Organization 3"},
    {"id": 00000, "name": "Organization 4"},
    {"id": 00000, "name": "Organization 5"}
]

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S+03:00"
TIMEZONE = "Europe/Istanbul" 