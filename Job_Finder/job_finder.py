from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def scrape_indeed(query, location, limit=10):
    jobs = []

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Adjust path if needed
    service = Service("chromedriver.exe")  # put path to chromedriver if not in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f"https://www.indeed.com/jobs?q={query}&l={location}"
    driver.get(url)
    time.sleep(3)  # wait for page to load

    job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")

    for card in job_cards[:limit]:
        try:
            title = card.find_element(By.CLASS_NAME, "jobTitle").text
        except:
            title = "N/A"
        try:
            company = card.find_element(By.CLASS_NAME, "companyName").text
        except:
            company = "N/A"
        try:
            location = card.find_element(By.CLASS_NAME, "companyLocation").text
        except:
            location = "N/A"
        try:
            link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link
        })

    driver.quit()
    return jobs

# ---------------------------
# Run Scraper
# ---------------------------
if __name__ == "__main__":
    query = "site reliability engineer"
    location = "India"
    results = scrape_indeed(query, location, limit=10)

    if not results:
        print("No jobs found.")
    else:
        for job in results:
            print("Title:", job["title"])
            print("Company:", job["company"])
            print("Location:", job["location"])
            print("Link:", job["link"])
            print("-" * 50)
