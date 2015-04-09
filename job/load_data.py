import csv
csv_filepathname="/home/oxfordadmin/oxford/job/new.csv"
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'OSHPD_ID':
        company = HealthCareCompany()
        company.oshpd_id = row[1]
        company.name = row[2]
        company.address = row[3]
        company.city = row[4]
        company.zipcode = row[5]
        company.county_code = row[6]
        company.county_name = row[7]
        company.status = row[8]
        company.status_date = row[9]
        company.license_type = row[10]
        company.license_category = row[11]
        company.link = row[12]
        company.full_address = row[3] + ', ' + row[4] + ', ' + row[5]
        company.npi = row[14]
        company.cahsah = row[15]
        company.latitude = row[16]
        company.longitude = row[17]
        company.save()