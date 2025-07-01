from api.organisation import OrganisationClient
from config.settings import start_date, end_date
from core.auth import tgt

def get_all_powerplants(selected_organization_ids):
    client = OrganisationClient(tgt_token=tgt, start_date=start_date, end_date=end_date)
    all_powerplants = []

    for org_id in selected_organization_ids:
        powerplants = client.fetch_registered_powerplants(org_id)
        for plant in powerplants:
            plant['organization_id'] = org_id
        all_powerplants.extend(powerplants)

    return all_powerplants

def get_all_uevcbs(power_plants):
    client = OrganisationClient(tgt_token=tgt, start_date=start_date, end_date=end_date)
    all_uevcbs = []

    for item in power_plants:
        power_plant_id = item["id"]
        if power_plant_id:
            uevcbs = client.fetch_uevcbs_by_powerplant_id(power_plant_id)
            for u in uevcbs:
                u['powerplant_id'] = power_plant_id
                u['organization_id'] = item["organization_id"]
            all_uevcbs.extend(uevcbs)
    return all_uevcbs
