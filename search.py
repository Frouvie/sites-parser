import googlesearch

LANGUAGE = "en"

def request_input():
    query = input("Enter your search query: ")
    number_results = int(input("Enter the number of results you want: "))

    return query, number_results


def search_sites():
    query, number_results = request_input()

    search_result = googlesearch.search(query,
                           num_results=number_results,
                           lang=LANGUAGE)
    
    return search_result
