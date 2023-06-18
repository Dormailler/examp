from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_page_count(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav",class_="css-jbuxu0")
    pages = pagination.find_all("div",class_="css-tvvxwd",recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("총",pages,"페이지")
    results = []
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    for page in range(pages):
        url = f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}"
        browser.get(url)
        print("요청url",url)
        soup = BeautifulSoup(browser.page_source,"html.parser")
        job_list = soup.find('ul',class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li',recursive=False)
        for job in jobs:
            zone = job.find('div',class_="mosaic-zone")
            if zone == None:
                # h2 = job.find('h2',class_="jobTitle")
                # a = h2.find('a')
                anchor = job.select_one('h2 a')
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span",class_="companyName")
                location = job.find("div",class_="companyLocation")
                job_data = {
                            'link' : f"https://kr.indeed.com{link}",
                            'company': company.string.replace(","," "),
                            'location' : location.string.replace(","," "),
                            'position' : title.replace(","," ")
                        }
                results.append(job_data)
    return results