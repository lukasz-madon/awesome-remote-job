import re
import pandas as pd
SHEET_ID = '1TLJSlNxCbwRNxy14Toe1PYwbCTY7h0CNHeer9J0VRzE'
SHEET_GID = '1279011369'

class Company:
    def __init__(self) -> None:
        self.name = ''
        self.website = ''
        self.nb_of_employees = 0
        self.description = ''
        self.country = ''

def read_companies(privious_companies):
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_GID}&headers=0'
    data_resutl = pd.read_csv(url, skiprows=[0,1,2])
    companies = []
    for element in data_resutl.values:
        company = Company()
        company.name = element[2]
        company.website = element[16]
        company.nb_of_employees = element[7]
        company.description = element[8]
        company.country = element[10]
        if company.name.lower() not in privious_companies:
            companies.append(company)
    return companies

def get_privious_companies():
    def get_sections(s):
        for sec in s.split('\n## '):
            yield sec if sec.startswith('## ') else '## '+sec

    file = open('./README.md','r')
    contents = file.read()
    list_companies = []
    for i, sec in enumerate(get_sections(contents)):
        if i == 14:
            list_companies = sec.splitlines()[1:]
    return list_companies

privious_companies = get_privious_companies()
company_names = map(lambda a: re.findall(r'\[([^]]*)\]', a)[0].lower(), privious_companies)
companies_need_to_add = read_companies(list(company_names))
for element in companies_need_to_add:
    item = f'  1. [{element.name}]({element.website}) - {element.description}'
    privious_companies.append(item)

print(privious_companies)
## Update list to README.md file