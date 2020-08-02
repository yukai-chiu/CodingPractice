# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        if not startUrl:
            return []
        host_name =  "http://" + startUrl[7:].split("/",1)[0]
        crawl_list = []
        visited = set()
        queue = deque([startUrl])
        visited.add(startUrl)
        
        while queue:
            curr = queue.pop()  
            crawl_list.append(curr)
            crawl = htmlParser.getUrls(curr)
            for url in crawl:
                if host_name in url and url not in visited:
                    visited.add(url)
                    queue.append(url)

        return crawl_list