from bs4 import BeautifulSoup
import requests

WHITE = "\033[0;37m"
END = "\033[0m"

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
  "q": "istanbul weather",
  "hl": "tr",

}

response = requests.get('https://www.google.com/search', headers=headers, params=params).text
soup = BeautifulSoup(response, 'lxml')

tempature = soup.select_one('#wob_tm').text
info = soup.select_one('#wob_dc').text
location = soup.select_one('#wob_loc').text
image = "iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAl1JREFUOE+t019IU1EcB/Dv79wtx7CMwLWIipW+yN1LmRj9Adkm9A/qUbLUCpJA6EGjUlBDC3FQ+JAQwTQzeoh6K9CNUpD+og9e9GGmaBjuDkWKkbV2f3Gv03QrWep5+cE55/f5nfO79xDWedA6e0gCucfiAIujAFtAQsGRiJ8IWqqFl4H82noThOsATH8AHoDgU3R4bqKioiVtNuP7bolNGTGzNtpRV6UmFloEuddaDkbr304yPOMY9348OxKDVEAEsbCHgX4Buu1rqHy6MGeAzCD0WMdB2JEI9k7uQ/vwCWi86CTVJOb7vsaqcoB4HuxLt/38IYV6J/ciOLsTGgSyMj5je3oIdwaKV8SW6FfbGqqaDbC19ULeyLT93fTc5lR7n7SPgW9ppoidAKaSGu97AnJXrcUTCfDQ+eqmXI3Eh7ViRj6hiMqqvUVM/Hg9QCLkU1lNs5uB7rWDPLZLimRRaW2tBTHrKCC2rR7lmKaJkw9vVb40vnLJjebjRHgGwob/RznCLC61N1Z2zrcxPs5VN+VJQJ1G4hABG1eCNUEcJemLJRZ98kvSWjrqr00seymJyZkBpRSM2rBbduhrNr/i06Pqlsv0mOlXxkCoD7vktn++5aULti7lICRcVl3yGX1+a0C5oseQS75rFAgonYjhnloo96UEZr5S7KTxAdXlfK4n2P3Kfj1OuWXjf7UFBk+zoDfhAnkqJdDmHyzWr6x6nNnGFbuUB3oMF8oXDbB7MKhfWXU7H6UEbnkR3GQ2R3NCnpy38RPtMXrocn4yWtA9lB+NmodmjmV/TQR/AyTe0hCBTifwAAAAAElFTkSuQmCC"

print(f"|image={image}")
print("---")
print(f'{WHITE}Lokasyon: {END}{location}')
print(f'{WHITE}Hava: {END}{info}')
print(f'{WHITE}Sıcaklık: {END}{tempature}')