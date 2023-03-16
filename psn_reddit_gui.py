import praw
import PySimpleGUI as sg
from sale_md import get_comments
from psn_scraper import PSNScraper



if __name__ == '__main__':
    reddit = praw.Reddit()

    #Define the window's contents
    layout = [[sg.Text("Category")],
            [sg.Input(key='category')],
            [sg.Text("Reddit URL")],
            [sg.Input(key='reddit_url')],
            [sg.Text('Platform')],
            [sg.Input(key='platform')],
            [sg.Button('Ok'), sg.Button('Quit')]]
    
    #Create the window
    window = sg.Window('PSN Sales Generator', layout)

    #Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == 'Ok':
            submission = reddit.submission(url=values['reddit_url'])

            psn_scraper = PSNScraper(values['category'], values['platform'].upper())
            psn_scraper.get_all_data()

            comments = get_comments(psn_scraper.products)

            for c in comments:
                ind = c.rfind('|')
                submission = submission.reply(c[0:ind])
    
    # Finish up by removing from the screen
    window.close()


    