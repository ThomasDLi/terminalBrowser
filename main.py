import prompt_toolkit.shortcuts as pts
from prompt_toolkit import print_formatted_text
from googlesearch import search
import wikipediaapi

wiki = wikipediaapi.Wikipedia('en')

searchquery = pts.input_dialog(
    title="Search Query",
    text="").run()

searchresults = search(searchquery)

wikisearch = wiki.page(searchquery)

wikiresults = (wikisearch.summary[0:200])

wikiresults += " ..."

if wikisearch.exists():
    pts.message_dialog(
        title='Answer To Your Question',
        text=wikiresults).run()
    showrest = pts.yes_no_dialog(

        title='Show Search Results?',
        text='Do you still want to see search results?'

    ).run()

    if showrest == True:
        for x in range(len(searchresults)):
            print(searchresults[x])

else:
    for x in range(len(searchresults)):
        print(searchresults[x])