from api.organisation import OrganisationClient
from core.auth import tgt
from config.settings import start_date, end_date

def get_matching_gzu_ids(organization_ids):
    client = OrganisationClient(tgt_token=tgt, start_date=start_date, end_date=end_date)

    powerplants_with_org_id = []
    for org_id in organization_ids:
        plants = client.fetch_registered_powerplants(org_id)
        for plant in plants:
            plant["organization_id"] = org_id
        powerplants_with_org_id.extend(plants)

    a3_list = client.fetch_realtime_powerplants()
    a1_eic_set = {plant['eic'] for plant in powerplants_with_org_id}

    matched = []
    for item in a3_list:
        if item["eic"] in a1_eic_set:
            matched.append({
                "gzu_id": item["id"],  # GZU ID
                "organization_id": next((p["organization_id"] for p in powerplants_with_org_id if p["eic"] == item["eic"]))
            })

    return matched
