from playwright.sync_api import sync_playwright, Playwright
import re
import pandas as pd

# Repeated codes for all comments scraping
pw = sync_playwright().start()

chrome = pw.chromium.launch(headless=False)

page = chrome.new_page()

page.goto("https://www.instagram.com/p/C2gNOssiC9B/?img_index=4") # exact link on each post

link_count = page.locator("css=.x1lliihq.x1plvlek").count() # using . to separate class names, sometimes it needs more than one, it's a lot of trial and error

team_links = []*link_count

for i in range(link_count):
    link = page.locator("css=.x1lliihq.x1plvlek").nth(i).inner_text()
    outdf = pd.DataFrame({'comment': [link]})
    team_links.append(outdf)
    
output1 = pd.concat(team_links) # inputting into a dataframe variable


output1.to_csv('/Users/davidli/Desktop/ND Mod3/Unstructured/Project/messi/3rd.csv', index=False)
















