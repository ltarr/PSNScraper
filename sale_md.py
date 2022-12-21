from psn_scraper import PSNScraper
import sys
import pandas as pd

def get_comments(products):
    textlimit = 8000

    df = pd.DataFrame([[prod.title, prod.price, prod.discountText] for prod in products], columns=['Title', 'Price', 'Discount'])

    md_tbl = df[['Title', 'Price', 'Discount']].to_markdown(index=False)

    md_tbl_lines = md_tbl.splitlines()

    titleLine = md_tbl_lines[0] + "\n" + md_tbl_lines[1]

    cmtLength = len(titleLine)

    comments = []
    cmt = titleLine

    for line in md_tbl_lines[2:]:
        cmtLength += len(line)
        if cmtLength < textlimit:
            cmt += "\n" + line
        else:
            comments.append(cmt)
            cmt = titleLine + "\n" + line
            cmtLength = len(cmt)
    else:
        comments.append(cmt)
    
    return comments

def process_data(products):
    comments = get_comments(products)

    with open(output_name, 'w', encoding='utf-8') as f:
        for x in comments:
            f.write(x)
            f.write("\n"*10)

if __name__ == '__main__':
    category = sys.argv[1]
    output_name = sys.argv[2]
    platform = sys.argv[3]

    psn_scraper = PSNScraper(category, platform)
    psn_scraper.get_all_data()

    process_data(psn_scraper.products)