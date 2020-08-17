import requests
import bs4
from time import sleep
from twilio.rest import Client


def text_me(job, company):
    account_sid = 'REDACTED'
    auth_token = 'REDACTED'
    client = Client(account_sid, auth_token)
    body = "There is a " + str(job) + " job available at " + str(company)
    client.messages.create(body=body, from_='REDACTED', to='REDACTED')


def endgame():
    company = "Endgame"
    r = requests.get('https://www.endgame.com/careers/career-openings')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    jobs = soup.select('li > div > span')
    looking_for = ['']
    avoid = ['']
    toApply = []
    for x in jobs:
        if any(word.lower() in x.text.lower() for word in looking_for):
            if any(excl.lower() not in x.text.lower() for excl in avoid):
                toApply.append(x.text)
    if len(toApply) > 0:
        for x in range(len(toApply)):
            text_me(toApply[x], company)


def cisco():
    company = "Cisco"
    r = requests.get('https://jobs.cisco.com/jobs/SearchJobs/csirt')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    jobs = soup.select('tbody > tr > td')
    split_jobs = []
    looking_for = ['']
    avoid = ['']
    location = ['']
    toApply = []

    for x in range(len(jobs)):
        if x % 5 == 0:
            split_jobs.append(jobs[x-5])
            split_jobs.append((jobs[x-2]))

    job_title = []
    job_location = []
    for x in range(len(split_jobs)):
        if x % 2 == 0:
            job_title.append(split_jobs[x])
        else:
            job_location.append(split_jobs[x])
    for x in range(len(job_title)):
        if any(title.lower() in job_title[x].text.lower() for title in looking_for):
            if not any(excl.lower() in job_title[x].text.lower() for excl in avoid):
                if any(loc.lower() in job_location[x].text.lower() for loc in location):
                    toApply.append(job_title[x].text)
    if len(toApply) > 0:
        for x in range(len(toApply)):
            text_me(toApply[x], company)


def crowdstrike():
    company = "Crowdstrike"
    r = requests.get('https://jobs.jobvite.com/crowdstrike/')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")

    jobs = soup.find_all('td', class_='jv-job-list-name')
    locations = soup.find_all('td', class_='jv-job-list-location')

    looking_for = ['']
    location = ['']

    toApply = []

    for x in range(len(jobs)):
        if any(title.lower() in jobs[x].text.lower() for title in looking_for):
            if any(loc.lower() in locations[x].text.lower() for loc in location):
                toApply.append(jobs[x].text)

    if len(toApply) > 0:
        for x in range(len(toApply)):
            text_me(toApply[x], company)


if __name__ == '__main__':
    while True:
        cisco()
        endgame()
        crowdstrike()
        sleep(86400)
