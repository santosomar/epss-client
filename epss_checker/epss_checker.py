'''
A client to retrieve the EPSS score for a CVE ID from the FIRST EPSS API.
Author: Omar Santos @santosomar
Version: 1.0
'''

# Import the required libraries
import requests
import sys

def get_epss_score(cve_id):
    url = f"https://api.first.org/data/v1/epss?cve={cve_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']:
            epss_info = data['data'][0]
            if 'epss' in epss_info:
                return epss_info['epss']
            else:
                return "EPSS score not found in the data dictionary"
        else:
            return "EPSS score not found in the response"
    else:
        return f"Failed to retrieve data. HTTP Status code: {response.status_code}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py CVE-XXXX-XXXX")
        sys.exit(1)
    
    cve_id = sys.argv[1]
    epss_score = get_epss_score(cve_id)
    print(f"The EPSS score for {cve_id} is: {epss_score}")

if __name__ == "__main__":
    main()
