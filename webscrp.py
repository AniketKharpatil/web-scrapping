from bs4 import BeautifulSoup
import requests

URL="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
htm_text=requests.get(URL)
soup=BeautifulSoup(htm_text.content,"lxml")
alljobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")


# no more of use as not sorted ==>print(jobs)
#cuz company name is inside hr tag inside li
#<h3 class="joblist-comp-name">
#   Larsen &amp; Toubro Infotech Ltd

  #  </h3>
for job in alljobs:
    publish_date = job.find('span', class_='sim-posted').text
    if 'few' in publish_date:

        comp_name = job.find("h3", class_="joblist-comp-name").text.replace(' ', '')
        skills = job.find('span', class_="srp-skills").text.replace(' ','')
        more_info=job.header.h2.a['href']
        space="******************************************************************************************************************************************************************************************************************************************************************************************************************************************"

        jobdata=(f"COMPANY NAME:{comp_name.strip()}\nSKILLS:{skills.strip()}\nMORE INFO:{more_info}\n\n{space}\n")
        print(jobdata)


