import random as r
import math as m
import requests

redeem_url = "https://discord.com/billing/partner-promotions/1180231712274387115"
api_url = "https://api.discord.gx.games/v1/direct-fulfillment"

# opera gx retrieves partnerid from native code that get some hashes or something
# but the code defaults to an equivalent of this function if window.opr is not defined so we'll use this one
def generateUUID():
	uid_mask = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx"
	get_e = lambda: m.floor(16 * r.uniform(0, 1)) | 8
	random_mask = "".join([hex(e)[2:] if isinstance(e, int) else e for e in [get_e() if l == "x" else ((3 & get_e() | 8) if l == "y" else l) for l in uid_mask]])
	return random_mask

headers = {
	"authority": "api.discord.gx.games",
	"content-type": "application/json",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
}

payload = {
	"partnerUserId": generateUUID()
}

print("Making request pls wait")
r = requests.post(api_url, json=payload, headers=headers)
if r.status_code == 200:
	link_url = f"{redeem_url}/{r.json()['token']}"
	print(f"Here is your link url : {link_url}")
else:
	print("Aw it did no work :c")
