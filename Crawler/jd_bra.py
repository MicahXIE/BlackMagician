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

def save_mongo(comments):

	for comment in comments:
		product_data = {}

		# colour
		# flush_data clean data
		product_data['product_color'] = flush_data(comment['productColor'])
		# size
		product_data['product_size'] = flush_data(comment['productSize'])
		# comment
		product_data['comment_content'] = flush_data(comment['content'])
		# create time 
		product_data['create_time'] = flush_data(comment['creationTime'])

		product_db.insert(product_data)

# data cleaning
def flush_data(data):

	if '肤' in data:
		return '肤色'
	if '黑' in data:
		return '黑色'
	if '紫' in data:
		return '紫色'
	if '粉' in data:
		return '粉色'
	if '蓝' in data:
		return '蓝色'
	if '白' in data:
		return '白色'
	if '灰' in data:
		return '灰色'
	if '槟' in data:
		return '香槟色'
	if '琥' in data:
		return '琥珀色'
	if '红' in data:
		return '红色'
	if '紫' in data:
		return '紫色'
	if 'A' in data:
		return 'A'
	if 'B' in data:
		return 'B'
	if 'C' in data:
		return 'C'
	if 'D' in data:
		return 'D'


"""
Search prod id
"""
def find_product_id(key_word):
	jd_url = 'https://search.jd.com/Search'
	product_ids = []
	# crawl the first 3 pages
	for i in range(1,3):
		param = {'keyword': key_word, 'enc': 'utf-8', 'page': i}
		response = requests.get(jd_url, params=param)

		# prod id
		ids = re.findall('data-pid="(.*?)"', response.text, re.S)
		product_ids += ids

	return product_ids

"""
get the comments
"""
def get_comment_message(product_id):
	urls = ['https://sclub.jd.com/comment/productPageComments.action?' \
			'callback=fetchJSON_comment98vv53282&' \
			'productId={}' \
			'&score=0&sortType=5&' \
			'page={}' \
			'&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(product_id, page) for page in range(1,11)]

	print("comment urls: ", urls)

	for url in urls:
		response = requests.get(url)
		html = response.text
		#delete the redundant chars
		html = html.replace('fetchJSON_comment98vv53282(','').replace(');','')
		data = json.load(html)
		comments = data['comments']

		# add one thread to save content to db
		t = threading.Thread(target=save_mongo, args=(comments,))
		t.start()



# thread lock
lock = threading.Lock()

# get comment thread
def spider_jd(ids):
	while ids:
		# add lock
		lock.acquire()
		# get the first element
		id = ids[0]
		# del element to prevent duplication
		del ids[0]
		# release lock
		lock.release()

		get_comment_message(id)


product_ids = find_product_id('胸罩')

for i in (1,5):
	# add one thread to get comment
	t = threading.Thread(target=spider_jd, args=(product_ids,))
	t.start()



color_arr = ['肤色', '黑色', '紫色', '粉色', '蓝色', '白色', '灰色', '香槟色', '红色']

color_num_arr = []
for i in color_arr:
	num = product_db.count({'product_color': i})
	color_num_arr.append(num)
	print("color: %s, num: %d" % (i, num))

colors = ['bisque', 'black', 'purple', 'pink', 'blue', 'white', 'grey', 'peru', 'red']

# draw the pic
patches, l_text, p_text = plt.pie(color_num_arr, labels=color_arr, colors=colors, 
								  labeldistance=1.1, autopct='%3.1f%%', shadow=False,
								  startangle=90, pctdistance=0.6)


for t in l_text:
	t.set_size(30)
for t in p_text:
	t.set_size(20)

plt.axis('equal')
plt.title('bra color proportion', fontproperties='SimHei')
plt.legend()
plt.show()

index = ["A", "B", "C", "D"]

value = []

for i in index:
	num = product_db.count({'product_size': i})
	value.append(num)

plt.bar(left=index, height=value, color="green", width=0.5)
plt.show()






