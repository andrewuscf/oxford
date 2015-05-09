import csv
from job.models import HealthCareCompany

csv_filepathname="/Users/Andrew/projects/oxford/job/test.csv"
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
        company.save()

companies = HealthCareCompany.objects.all().distinct('latitude', 'longitude')
for company in companies:
    print company

for lat in HealthCareCompany.objects.values_list('latitude', flat=True).distinct():
    company = HealthCareCompany.objects.filter(pk__in=HealthCareCompany.objects.filter(latitude=lat).values_list('id', flat=True))
    print company
