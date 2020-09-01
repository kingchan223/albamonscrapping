import requests
from bs4 import BeautifulSoup

URL = "http://www.albamon.com/search?Keyword=편의점"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    links = soup.find("div", {"class": "listPaging"}).find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("a")["title"]
    location = html.find("dd", {"class": "local"}).get_text()
    job_link_id = html.find("a")["href"]
    link = f"http://www.albamon.com{job_link_id}"
    print({"title": title, "location": location, "link": link})


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page + 1):
        print(f"scrapping albamon page{page}")
        result = requests.get(f"{URL}&page={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "booth"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)


def get_jobs():
    last_page = get_last_page()
    jobs = extract_job(last_page)
    return jobs
