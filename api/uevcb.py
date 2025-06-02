import requests
import json
from core.settings import BASE_URL, ENDPOINTS, START_DATE, END_DATE
from api.auth import tgt
from api.power_plants import get_santral_and_eic_by_orgId

def get_uevcb_by_power_plant_id(powerPlantId, startDate, endDate, TGT):
        try:
            response = requests.post(
                url= BASE_URL + ENDPOINTS["UEVCB_LIST"],
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "TGT": TGT
                },
                data=json.dumps({
                    "powerPlantId": powerPlantId,
                    "startDate": str(startDate),
                    "endDate": str(endDate),
                })
            )
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


start = START_DATE
end = END_DATE

organization_ids = [13119, 7902, 4069, 20880, 16287]

for org_id in organization_ids:
    data = get_santral_and_eic_by_orgId(org_id, start, end, tgt)

    if data and "items" in json.loads(data):
        print(f"\nOrganization ID: {org_id}")
        for plant in json.loads(data)["items"]:
            power_plant_id = plant["id"]
            print(f"Power Plant: {power_plant_id}, Name: {plant.get('name', '')}")

            uevcb_data = get_uevcb_by_power_plant_id(power_plant_id, start, end, tgt)
            if uevcb_data and "items" in json.loads(uevcb_data):
                for uevcb in json.loads(uevcb_data)["items"]:
                    print(f"UEVCB ID: {uevcb['id']}, Name: {uevcb.get('name', '')}")
            else:
                print("UEVÇV data not found or empty for this power plant.")

    else:
        print(f"Data not found or empty for this organization ID {org_id}.")

