import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    scrape infromation from LinkedIn profile, Manually scrape the LinkedIn profile
    """
    api_key = os.getenv("PROXYCURL_API_KEY")
    # api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    # headers = {'Authorization': 'Bearer ' + api_key}
    headers = {'Content-Type': 'application/json'}
    api_endpoint = linkedin_profile_url or 'https://gist.githubusercontent.com/hyungjunk/1d213fca608b77b2f8c6d664c75ee96a/raw/bc93b25bc6a732e5c73fc173d5c8625198392ca7/gistfile1.txt'
    params = {
        'linkedin_profile_url': 'https://www.linkedin.com/in/hyungjun-kim-34901b11b/',
    }
    return requests.get(api_endpoint, params=params, headers=headers).json()


if __name__ == "__main__":
    response = scrape_linkedin_profile('')
    print(response)
