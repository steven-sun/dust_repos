#/usr/bin/python3

# 辽宁省

import urllib.request
import urllib.error
import urllib

from bs4 import BeautifulSoup
import urllib3

def create_header():
	head = urllib3.util.make_headers(keep_alive=True, accept_encoding="gzip, deflate", user_agent='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36', basic_auth=None)
	head['Host'] = '218.60.147.121:8080'
	head['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	head['Accept-Encoding'] = 'gzip, deflate, sdch'
	head['Accept-Language'] = 'zh-CN,zh;q=0.8'

	return head


def track_info(tbody, fp):
	for people in tbody:
		info = people.h3.string + "， "
		tds = people.table.findAll('td')
		for td in tds:
			info += td.text + "， "
		tds = people.div.table.findAll('td')
		info += tds[2].text
		info += tds[3].text
		fp.write(info+"\n")
		
	return	
	
	
if __name__ == "__main__":
	
	url_prefix = 'http://218.60.147.121:8080/lnlxoa/govhall/lawFirmResult.jsp?pn='	
	result_file = 'liaoning_firm.txt'	
	
	fp = open(result_file, 'w')
	header = create_header()
	
	page_id = 1
	while True:
		print("Current page: %d" % page_id)
		url = url_prefix + repr(page_id)
		req = urllib.request.Request(url, headers=header)
		response = urllib.request.urlopen(req)
		soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'), 'lxml')
		info_soup = soup.findAll('div', attrs={"class":"zi36"})
		if info_soup:
			track_info(info_soup, fp)
		
		page_id += 1
		if page_id > 92:
			break
	
	fp.close()
	print("Done!")
