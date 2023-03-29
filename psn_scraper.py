import requests
from config import Config

class PSNProduct:
    """Represent product on sale"""

    def __init__(self, productName, url, price, discountText):
        self.productName = productName
        self.url = url
        self.title = f'[{productName}]({url})'
        self.price = price
        self.discountText = discountText



class PSNScraper:
    """Gets Data from PSN"""
    def __init__(self, category, platform):
        self.category = category
        self.platform = platform
        self.headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "x-psn-store-locale-override": "en-US"
        }
        self.products = []
        self.url = "https://web.np.playstation.com/api/graphql/v1//op"
        self.count = self.get_count()
    
    def get_all_data(self):
        res = []
        pages = self.count // 1000

        for i in range(pages+1):
            res.extend(self.get_data(i*1000))
        
        self.products.extend(res)

    
    def get_data(self, offset):
        rtn_data = []

        # Exit if no PSN SHA256.
        if Config.PSN_SHA_256 is None or Config.PSN_SHA_256 == '':
            print("Make sure your PSN SHA256 code is in the config file. Exiting program.")
            exit()
        
        querystring = {"operationName":"categoryGridRetrieve","variables":"{\"id\":\"" + self.category + "\",\"pageArgs\":{\"size\":1000,\"offset\":" + str(offset) + "},\"sortBy\":{\"name\":\"productName\",\"isAscending\":true},\"filterBy\":[\"targetPlatforms:" + self.platform + "\"],\"facetOptions\":[]}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"" + Config.PSN_SHA_256 + "\"}}"}

        response = requests.request("GET", self.url, headers=self.headers, params=querystring)

        data = response.json()

        if data is None:
            return rtn_data
        
        for p in data['data']['categoryGridRetrieve']['products']:
            productName = p['name'].replace('|', '')
            url = 'https://store.playstation.com/en-us/product/' + p['id']
            if p['price'] is not None:
                discountedPrice = p['price']['discountedPrice']
                discountText = p['price']['discountText']
                product  = PSNProduct(productName, url, discountedPrice, discountText)
                rtn_data.append(product)
            
        return rtn_data
    
    def get_count(self):
        querystring = {"operationName":"categoryGridRetrieve","variables":"{\"id\":\"" + self.category + "\",\"pageArgs\":{\"size\":1,\"offset\":0},\"sortBy\":{\"name\":\"productName\",\"isAscending\":true},\"filterBy\":[\"targetPlatforms:" + self.platform + "\"],\"facetOptions\":[]}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"" + Config.PSN_SHA_256 + "\"}}"}

        response = requests.request("GET", self.url, headers=self.headers, params=querystring)

        data = response.json()

        return data['data']['categoryGridRetrieve']['pageInfo']['totalCount']
