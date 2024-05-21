from urllib.request import urlopen
import re


def get_html_page_decoded(url):
    page = urlopen(url)
    html = page.read().decode()  # reads the page and decodes the page (because it is in UTF format which is unreadable.
    print(html)
    return html


html_scraped = get_html_page_decoded(url="http://olympus.realpython.org/profiles/poseidon")


title_index = html_scraped.find("<title>")
if title_index != -1:
    start_index = title_index + len("<title>")
    if html_scraped.find("</title>") != -1:
        end_index = html_scraped.find("</title>")
    else:
        end_index = html_scraped.find("</title >")
else:
    title_index_replace = html_scraped.find("<title >")
    start_index = title_index_replace + len("<title >")
    if html_scraped.find("</title>") != -1:
        end_index = html_scraped.find("</title>")
    else:
        end_index = html_scraped.find("</title >")


title = html_scraped[start_index:end_index]  # title content grabbed with slicing (This is a bad way of doing it.)
title_tag_including_content = re.findall("<title.*>", html_scraped, re.IGNORECASE)

print(title_tag_including_content)
title_content = re.findall("", title_tag_including_content[0], re.IGNORECASE)


