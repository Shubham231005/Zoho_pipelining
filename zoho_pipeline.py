import sqlite3
import requests
from datetime import datetime
import json 

ZOHO_TOKEN = "1000.9d10531dc7333d5eed0071042d31acfc.7e8eba94061dca0ef7eeb4d32fe2dce4"

ORG_ID = "60059676751"
WORKSPACE_ID = "497216000000012008"
TABLE_ID = "497216000000012191"


def normalize_to_zoho_timestamp(ts):
    if "," in ts:
        return ts
    dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%d %b, %Y %H:%M:%S")


def push_data_to_zoho():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT page, device, browser, time_spent, timestamp FROM visitors")
    rows = cur.fetchall()
    conn.close()

    print("📦 ROWS FOUND:", len(rows))

    data = []
    for r in rows:
        data.append({
            "page": r[0],
            "device": r[1],
            "browser": r[2],
            "time_spent": int(r[3]),
            "timestamp": normalize_to_zoho_timestamp(r[4])
        })

    if not data:
        print("❌ No data to push")
        return

    url = (
        f"https://www.zohoapis.in/analytics/v2/orgs/{ORG_ID}"
        f"/workspaces/{WORKSPACE_ID}/tables/{TABLE_ID}/rows"
    )

    headers = {
        "Authorization": f"Zoho-oauthtoken {ZOHO_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {"rows": data}

    response = requests.post(url, headers=headers, json=payload)

    print("🔑 STATUS:", response.status_code)
    print("📨 RESPONSE:", response.text)


if __name__ == "__main__":
    push_data_to_zoho()
