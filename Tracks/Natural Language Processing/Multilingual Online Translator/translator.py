import requests
import sys
from http.client import responses
from bs4 import BeautifulSoup

s = requests.Session()


def url_request(request_to_site, language, check, word):
    txt_file = open(f'{word}.txt', 'a+', encoding='utf-8')

    if check:
        try:
            r = s.get(request_to_site, headers=headers)
            if r.status_code == 404:
                print(f'Sorry, unable to find {word}')
                sys.exit()
        except requests.ConnectionError:
            print("Something wrong with your internet connection")
            sys.exit()

    else:
        try:
            r = requests.get(request_to_site, headers=headers)
            if r.status_code == 404:
                print(f'Sorry, unable to find {word}')
                sys.exit()
        except requests.ConnectionError:
            print("Something wrong with your internet connection")
            sys.exit()

    if not check:
        print(r.status_code, responses[r.status_code])
    soup = BeautifulSoup(r.content, 'html.parser')

    print(language, 'Translations')
    txt_file.write(language + " Translations\n")
    result = []
    for elem in soup.find_all('a', {"class": 'translation'}):
        result.append(elem.text.strip())

    for w in result[1:6]:
        print(w)
        txt_file.write(w + "\n")
        if check:
            break
    print()
    txt_file.write("\n")
    print(language, 'Examples')
    txt_file.write(language + " Examples\n")
    result_from = soup.find_all('div', {"class": "src ltr"})
    result_to = soup.find_all('div', {"class": ["trg ltr", "trg rtl arabic", "trg rtl"]})
    result_from = [x.text.strip() for x in result_from]
    result_to = [x.text.strip() for x in result_to]

    for elem in zip(result_from[:5], result_to[:5]):
        print(elem[0])
        txt_file.write(elem[0] + "\n")
        print(elem[1])
        txt_file.write(elem[1] + "\n")
        print()
        txt_file.write("\n")
        if check:
            break
    txt_file.close()


# print("""Hello, you're welcome to the translator. Translator supports:
# 1. Arabic
# 2. German
# 3. English
# 4. Spanish
# 5. French
# 6. Hebrew
# 7. Japanese
# 8. Dutch
# 9. Polish
# 10. Portuguese
# 11. Romanian
# 12. Russian
# 13. Turkish""")
# print("Type the number of your language:")
# translate_from = int(input())
# print("Type the number of language you want to translate to or '0' to translate to all languages:")
# translate_to = int(input())
# print("Type the word you want to translate:")
# word = input()
languages = {'1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish', '5': 'French',
             '6': 'Hebrew', '7': 'Japanese', '8': 'Dutch', '9': 'Polish', '10': 'Portuguese',
             '11': 'Romanian', '12': 'Russian', '13': 'Turkish'}
translate_from = sys.argv[1]
translate_to = sys.argv[2]
input_word = sys.argv[3]

if translate_to.capitalize() not in languages.values():
    if translate_to != "all":
        print("Sorry, the program doesn't support " + translate_to)
        sys.exit()

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://context.reverso.net/translation/'
if translate_to == "all":
    pass
    for i in range(1, 14):
        req = url + translate_from + "-" + languages[f'{i}'].lower() + "/" + input_word
        url_request(req, languages[f'{i}'], True, input_word)
else:
    req = url + translate_from + "-" + translate_to + "/" + input_word
    url_request(req, translate_to.capitalize(), False, input_word)
# languages = {'1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish', '5': 'French',
#              '6': 'Hebrew', '7': 'Japanese', '8': 'Dutch', '9': 'Polish', '10': 'Portuguese',
#              '11': 'Romanian', '12': 'Russian', '13': 'Turkish'}
#
# headers = {'User-Agent': 'Mozilla/5.0'}
# url = 'https://context.reverso.net/translation/'
# if translate_to == 0:
#     for i in range(1, 14):
#         req = url + languages[f'{translate_from}'].lower() + "-" + languages[f'{i}'].lower() + "/" + word
#         url_request(req, languages[f'{i}'], True, word)
# else:
#     req = url + languages[f'{translate_from}'].lower() + "-" + languages[f'{translate_to}'].lower() + "/" + word
#     url_request(req, languages[f'{translate_to}'], False, word)
