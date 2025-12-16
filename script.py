import requests

ZOHO_TOKEN = "1000.8ed7418d8efd07c151ffe0952c01f76b.9445d91d094a951c8a809a2d19a23eb9"

headers = {
    "Authorization": f"Zoho-oauthtoken {ZOHO_TOKEN}"
}

r = requests.get(
    "https://analyticsapi.zoho.in/restapi/v2/orgs",
    headers=headers
)

print(r.status_code)
print(r.text)
