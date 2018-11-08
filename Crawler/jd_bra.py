import requests
import re

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

    	t = threading.Thread(target=save_mongo, args=(comments,))
    	t.start()

# mongo service
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#db
db = client.jd
#product db table
product_db = db.product

def save_mongo(comments):
	


