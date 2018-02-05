import pprint, os, csv, json, pickle, urllib, html5lib
from bs4 import BeautifulSoup
from mozscape import Mozscape
pp = pprint.PrettyPrinter(indent=4)

def find_all_articles():

	article_list = []
	count = 0;
	for page_num in range(1,68):
		base_url = 'http://claremontindependent.com/page/%d/' % page_num
		r = urllib.urlopen(base_url).read()
		soup = BeautifulSoup(r, "html5lib")
		
		for article in soup.find_all("article"):
			print(count)
			entry = [count, article.div.h3.a.string, article.div.h3.a.get("href")]
			article_list.append(entry)
			count += 1
				
	return(article_list)

def get_article_text( article_url ):

	r = urllib.urlopen(article_url)
	soup = BeautifulSoup(r, "html5lib")
	body = soup.find(attrs={"class": "entry-content"})
	paragraphs = body.get_text()
	text, seperator, attribution = paragraphs.partition("\n\n")
	
	return(text)

def get_article_backlinks( article_url ):
	
	client = Mozscape('mozscape-53cf2bb871', '694d6aba7224dc5fd11b6ed7c73e20e1')
	backlinks = client.links('http://claremontindependent.com/pitzer-college-ra-white-people-cant-wear-hoop-earrings/', 
				scope ='page_to_page',
				sort ='domain_authority',
				filters = ['external'],
				linkCols = 0,
				targetCols = Mozscape.UMCols.url)

	pp.pprint(backlinks)
	return(backlinks)

def write_data( data , filename ):
	""" Takes in list of list made in read_data and puts it in new csv file.
	"""
	csvfile = open( filename , 'w' )
	writer = csv.writer( csvfile )
	for row in data:
		writer.writerow([unicode(s).encode("utf-8") for s in row])
	
	csvfile.close()
	del writer

	pass

def load_pickle( filename ):

	corpus = pickle.load(open('CI-Articles-Corpus'))

	return(corpus)

def main():

	# article_list = find_all_articles()
	# write_data( article_list, os.getcwd() + "/CI-Articles.csv" )

	with open('CI-Articles.csv', 'rb') as csvfile:
		article_list = csv.reader(csvfile)

		corpus = []
		for article in article_list:
			title = article[1]
			body = get_article_text(article[2])
			corpus.append([article[0], article[1],body])
			print(article[0])
			# backlinks = get_article_backlinks(article[2])
		
	pp.pprint(corpus)
	with open('CI-Articles-Corpus','wb') as f:
		pickle.dump(corpus, f)

	# corpus_load = load_pickle('CI-Articles-Corpus')
	# pp.pprint(corpus_load)

	pass

main()