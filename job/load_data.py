import csv
import time
from models import HealthCareCompany
csv_filepathname="/home/oxfordadmin/oxford/job/companies.csv"
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'OSHPD_ID':
        company = HealthCareCompany()
        company.oshpd_id = row[0]
        company.name = row[1]
        company.address = row[2]
        company.city = row[3]
        company.zipcode = row[4]
        company.county_code = row[5]
        company.county_name = row[6]
        company.status = row[7]
        company.status_date = row[8]
        company.license_type = row[9]
        company.license_category = row[10]
        company.link = row[11]
        company.full_address = row[2] + ', ' + row[3] + ', ' + row[4]
        company.npi = row[13]
        company.cahsah = row[14]
        company.latitude = row[15]
        company.longitude = row[16]
        company.save()