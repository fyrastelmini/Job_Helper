import os
from bs4 import BeautifulSoup
import requests
import azure.functions as func


def extract_div_content_linkedin(url, div_class):
    # Send a GET request to the URL
    response = requests.get(url, timeout=5000)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the specific div based on its ID
        target_div = soup.find("div", {"class": div_class})

        # Check if the div is found
        if target_div:
            # Extract and print the content of the div

            job_title = (
                target_div.find("h1", class_="top-card-layout__title")
                .text.strip()
                .split("Login & Sign Up")[0]
            )
            company_name = target_div.find(
                "a", class_="topcard__org-name-link"
            ).text.strip()
            location = target_div.find(
                "span", class_="topcard__flavor--bullet"
            ).text.strip()
            return {
                "job_title": job_title,
                "company_name": company_name,
                "location": location,
                "URL": url,
            }
        else:
            print(f"Div with class '{div_class}' not found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    url = req_body.get("url")

    # Extract information from the URL
    div_class = (
        "top-card-layout__entity-info-container flex flex-wrap papabear:flex-nowrap"
    )
    text = extract_div_content_linkedin(url, div_class)


    return func.HttpResponse(text, status_code=200)