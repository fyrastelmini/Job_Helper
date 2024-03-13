def test_init():
    assert True == True


from app import extract_div_content_linkedin


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
