def url_check(url):

    PREFIX_STRING = "//"

    start_of_url = url[0:4]

    if start_of_url != "http":
        url_check = PREFIX_STRING + url

    return
