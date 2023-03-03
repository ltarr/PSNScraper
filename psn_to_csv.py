from psn_scraper import PSNScraper
import sys
import pandas as pd

def process_csv(products, output_name):
    df = pd.DataFrame([[prod.productName, prod.url, prod.price, prod.discountText] for prod in products], columns=['Title', 'URL', 'Price', 'Discount'])

    df.to_csv(output_name, index=False)

if __name__ == '__main__':
    category = sys.argv[1]
    platform = sys.argv[2]
    output_name = sys.argv[3]
    

    psn_scraper = PSNScraper(category, platform)
    psn_scraper.get_all_data()

    process_csv(psn_scraper.products, output_name)