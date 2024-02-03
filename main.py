import parse
from search import search_sites

path = "C:/Users/User/Downloads/list.txt"

def google_search():
    links = search_sites()
    tags = parse.parse_sites(links)
    
    for tag in tags:
        text = tag.string
        
        if text == None:
            continue

        with open(path, "a") as file:
            file.write("\n")
            file.write(text)


if __name__ == "__main__":
    google_search()