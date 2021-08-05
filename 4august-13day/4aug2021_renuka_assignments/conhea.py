import csv
headercontent=["name","roll"]
studentdata=[
    {"name":"renuka","roll":22},
    {"name":"vishnu","roll":23},
    {"name":"anu","roll":24},
    {"name":"renuka","roll":22},
    {"name":"dharani","roll":22},
    {"name":"sri","roll":22},
]
with open('student.csv','w+',encoding='UTF8',newline='') as s:
    writer=csv.DictWriter(s,fieldnames=headercontent)
    writer.writeheader()
    writer.writerows(studentdata)