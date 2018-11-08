import requests
import re
import pymongo
from pylab import *
import threading
import json

# mongo service
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
#db
db = client.jd
#product db table
product_db = db.product


color_arr = ['肤色', '黑色', '紫色', '粉色', '蓝色', '白色', '灰色', '香槟色', '红色']

color_num_arr = []
for i in color_arr:
	num = product_db.count({'product_color': i})
	color_num_arr.append(num)
	print("color: %s, num: %d" % (i, num))

colors = ['bisque', 'black', 'purple', 'pink', 'blue', 'white', 'grey', 'peru', 'red']

# draw the pic
#patches, l_text, p_text = plt.pie(color_num_arr, labels=colors, colors=colors, 
#								  labeldistance=1.1, autopct='%3.1f%%', shadow=False,
#								  startangle=90, pctdistance=0.6)

#for t in l_text:
#	t.set_size(30)
#for t in p_text:
#	t.set_size(20)

#plt.axis('equal')
#plt.title('bra color proportion', fontproperties='SimHei')
#plt.legend()
#plt.show()

axis = [1, 2, 3, 4]
index = ["A", "B", "C", "D"]

value = []

for i in index:
	num = product_db.count({'product_size': i})
	value.append(num)

plt.bar(left=axis, height=value, color="green", width=0.5)
plt.xticks(axis, index)
plt.show()