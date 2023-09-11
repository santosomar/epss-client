'''
EPSS Checker: A client to retrieve the EPSS score for a CVE ID from the FIRST EPSS API.
Author: Omar Santos @santosomar
Version: 1.0
'''

# Import the required libraries
import requests
import argparse

def get_epss_score(cve_id):
    '''
    This function retrieves the EPSS score for a CVE ID from the FIRST EPSS API.
    Parameters:
    cve_id (str): The CVE ID to retrieve the EPSS score for.
    '''
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
    parser = argparse.ArgumentParser(description="""
 EPSS-Checker
 Author: @santosomar 
 A tool to fetch EPSS scores for CVEs from the FIRST EPSS API.""", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('cve_id', help='The CVE identifier to query (format: CVE-XXXX-XXXX)')
    parser.add_argument('-s', '--silent', action='store_true', help='Only display the EPSS score, without any additional text')
    
    args = parser.parse_args()
    
    epss_score = get_epss_score(args.cve_id)
    
    if args.silent:
        print(epss_score)
    else:
        print(f"The EPSS score for {args.cve_id} is: {epss_score}")

if __name__ == "__main__":
    main()
