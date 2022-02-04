from bs4 import BeautifulSoup
import requests
import csv



def get_prices():
    stickers = bs.find_all("div",  class_='well result-box nomargin')
    sticker_name_second = None
    for sticker in stickers:
        try:
            sticker_name = sticker.find('h3').text
            try:
                sticker_name_second = sticker.find('h4').text
            except:
                pass
            if sticker_name_second is not None:
                sticker_name = sticker_name + ' | ' + sticker_name_second
            sticker_price = sticker.find('div', class_="price").text[:-5].replace(',','.').replace(' ','')[1:]
            print(f"{sticker_name} {sticker_price}")
            info = (sticker_name, sticker_price)
            csv.writer(f).writerow(info)
            sticker_name_second = None
        except:
            print('\nПропущен\n')
            pass

if __name__=="__main__":
    f = open("price_table.csv", "a", newline="")
    # range 13 or 72
    for i in range(1,13):
        print(f"--------------PAGE #{i}---------------")
        url = f"https://csgostash.com/stickers/regular?name=&sticker_type=any&rarity_contraband=1&rarity_covert=1&rarity_legendary=1&rarity_mythical=1&rarity_rare=1&container=any&sort_agg=avg&sort=price_steam_agg&order=desc&page={i}"
        page = requests.get(url)
        bs = BeautifulSoup(page.text, "lxml")
        get_prices()
    for i in range(1,72):
        print(f"--------------PAGE #{i}---------------")
        url = f"https://csgostash.com/stickers/tournament?page={i}"
        page = requests.get(url)
        bs = BeautifulSoup(page.text, "lxml")
        get_prices()
    f.close()


#print(bs.title.text)
#print(one_sticker)


