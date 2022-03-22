import webbrowser

url = 'https://www.google.de/?q='
search = input("Please enter something you want to search via Google:")
webbrowser.get('firefox').open_new_tab(url+search)
