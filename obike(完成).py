
import requests
import xlwt
import json



workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('obike')

worksheet.write(0, 0, label='站名')
worksheet.write(0, 1, label='地址')
worksheet.write(0, 2, label='數量')
worksheet.write(0, 3, label='可借')
worksheet.write(0, 4, label='可停')
worksheet.write(0, 5, label='經度')
worksheet.write(0, 6, label='緯度')


url = "http://tbike-data.tainan.gov.tw/Service/StationStatus/Json"

bike = requests.get(url).text 

data = json.loads(bike)
val1 = 1
val2 = 1
val3 = 1
val4 = 1
val5 = 1
val6 = 1
val7 = 1

for list_item in data:
    for key, value in list_item.items():
        if key == "StationName":
            worksheet.write(val1, 0, value)
            val1 += 1
        elif key == "Address":
            worksheet.write(val2, 1, value)
            val2 += 1
        elif key == "Capacity":
            worksheet.write(val3, 2, value)
            val3 += 1
        elif key == "AvaliableBikeCount":
            worksheet.write(val4, 3, value)
            val4 += 1
        elif key == "AvaliableSpaceCount":
            worksheet.write(val5, 4, value)
            val5 += 1
        elif key == "Longitude":
            worksheet.write(val6, 5, value)
            val6 += 1
        elif key == "Latitude":
            worksheet.write(val7, 6, value)
            val7 += 1
        else:
            pass
        
workbook.save('obike.xls')












