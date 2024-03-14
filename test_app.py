def test_init():
    assert True == True


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

def test_linkedin():
    test_url = "https://www.linkedin.com/jobs/view/3817203204/"
    div_class = (
        "top-card-layout__entity-info-container flex flex-wrap papabear:flex-nowrap"
    )
    test_output = {
        "job_title": "Data Scientist AI",
        "company_name": "Cephalgo",
        "location": "France",
        "URL": test_url,
    }
    assert extract_div_content_linkedin(test_url, div_class) == test_output
