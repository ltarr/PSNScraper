from psn_scraper import PSNScraper
import argparse
import pandas as pd

def process_csv(products, output_name):
    df = pd.DataFrame([[prod.productName, prod.url, prod.price, prod.discountText] for prod in products], columns=['Title', 'URL', 'Price', 'Discount'])

    df.to_csv(output_name, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
    Get PSN sale results into a csv file. 
    ''')

    parser.add_argument('category',
                        help='PSN Sale Category')
    parser.add_argument('platform',
                        help="Platform (PS4 or PS5)")
    parser.add_argument('output_name',
                        help='Name of output csv file')
    
    args = parser.parse_args()
    
    psn_scraper = PSNScraper(args.category, args.platform)
    psn_scraper.get_all_data()

    process_csv(psn_scraper.products, args.output_name)