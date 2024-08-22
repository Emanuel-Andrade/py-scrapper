# type: ignore
import re
import json
from pathlib import Path
from time import sleep

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--log-level=3")

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service()

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 60

    options = ()
    browser = make_chrome_browser(*options)

    browser.get("https://veri.bet/odds-picks?filter=upcoming")

    WAIT_TO_ODDS = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.ID, "odds-picks"))
    )

    html = browser.page_source

    parsed_data = BeautifulSoup(html, "html.parser")
    odds = parsed_data.select("#odds-picks .col.col-md")

    all_odds = []
    index = 0
    for odd in odds:
        has_draw = list(odd.findAll("tr"))[15].findAll("span") != []
        all_odds.append([])
        turns = 6
        if has_draw:
            turns = 7
        for i in range(turns):
            match i:
                case 0:
                    all_odds[index].append(
                        {
                            "sport_league": list(odd.findAll("tr"))[14]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "event_date_utc": list(odd.findAll("tr"))[14]
                            .findAll("span")[1]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team1": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team2": list(odd.findAll("tr"))[9]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "pitcher": "",
                            "period": list(odd.findAll("tr"))[0]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", "")
                            .replace("ODDS", ""),
                            "line_type": "moneyline",
                            "price": list(odd.findAll("tr"))[4]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "side": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "spread": 0,
                        }
                    )
                case 1:
                    all_odds[index].append(
                        {
                            "sport_league": list(odd.findAll("tr"))[14]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "event_date_utc": list(odd.findAll("tr"))[14]
                            .findAll("span")[1]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team1": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team2": list(odd.findAll("tr"))[9]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "pitcher": "",
                            "period": list(odd.findAll("tr"))[0]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", "")
                            .replace("ODDS", ""),
                            "line_type": "moneyline",
                            "price": list(odd.findAll("tr"))[10]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "side": list(odd.findAll("tr"))[8]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team": list(odd.findAll("tr"))[8]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "spread": 0,
                        }
                    )
                case 2:
                    all_odds[index].append(
                        {
                            "sport_league": list(odd.findAll("tr"))[14]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "event_date_utc": list(odd.findAll("tr"))[14]
                            .findAll("span")[1]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team1": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team2": list(odd.findAll("tr"))[9]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "pitcher": "",
                            "period": list(odd.findAll("tr"))[0]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", "")
                            .replace("ODDS", ""),
                            "line_type": "spread",
                            "price": re.findall(
                                r"\((.*?)\)",
                                list(odd.findAll("tr"))[5]
                                .findAll("span")[0]
                                .text.replace("\t", "")
                                .replace("\n", ""),
                            ),
                            "side": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "spread": list(odd.findAll("tr"))[5]
                            .findAll("span")[0]
                            .text.split("(")[0]
                            .replace("\n", "")
                            .replace("\t", ""),
                        }
                    )
                case 3:
                    all_odds[index].append(
                        {
                            "sport_league": list(odd.findAll("tr"))[14]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "event_date_utc": list(odd.findAll("tr"))[14]
                            .findAll("span")[1]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team1": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team2": list(odd.findAll("tr"))[9]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "pitcher": "",
                            "period": list(odd.findAll("tr"))[0]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", "")
                            .replace("ODDS", ""),
                            "line_type": "spread",
                            "price": re.findall(
                                r"\((.*?)\)",
                                list(odd.findAll("tr"))[11]
                                .findAll("span")[0]
                                .text.replace("\t", "")
                                .replace("\n", ""),
                            ),
                            "side": list(odd.findAll("tr"))[8]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team": list(odd.findAll("tr"))[8]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "spread": list(odd.findAll("tr"))[11]
                            .findAll("span")[0]
                            .text.split("(")[0]
                            .replace("\n", "")
                            .replace("\t", ""),
                        }
                    )
                case 4:
                    all_odds[index].append(
                        {
                            "sport_league": list(odd.findAll("tr"))[14]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "event_date_utc": list(odd.findAll("tr"))[14]
                            .findAll("span")[1]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team1": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team2": list(odd.findAll("tr"))[9]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "pitcher": "",
                            "period": list(odd.findAll("tr"))[0]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", "")
                            .replace("ODDS", ""),
                            "line_type": "over/under",
                            "price": re.findall(
                                r"\((.*?)\)",
                                list(odd.findAll("tr"))[6]
                                .findAll("span")[0]
                                .text.replace("\t", "")
                                .replace("\n", ""),
                            ),
                            "side": list(odd.findAll("tr"))[6]
                            .findAll("span")[0]
                            .text.split("(")[0]
                            .replace("\n", "")
                            .replace("\t", "")
                            .__contains__("U")
                            and "Under"
                            or "Over",
                            "team": "Total",
                            "spread": list(odd.findAll("tr"))[6]
                            .findAll("span")[0]
                            .text.split("(")[0]
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("O", "")
                            .replace("U", ""),
                        }
                    )
                case 5:
                    all_odds[index].append(
                        {
                            "sport_league": list(odd.findAll("tr"))[14]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "event_date_utc": list(odd.findAll("tr"))[14]
                            .findAll("span")[1]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team1": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team2": list(odd.findAll("tr"))[9]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "pitcher": "",
                            "period": list(odd.findAll("tr"))[0]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", "")
                            .replace("ODDS", ""),
                            "line_type": "over/under",
                            "price": re.findall(
                                r"\((.*?)\)",
                                list(odd.findAll("tr"))[12]
                                .findAll("span")[0]
                                .text.replace("\t", "")
                                .replace("\n", ""),
                            ),
                            "side": list(odd.findAll("tr"))[12]
                            .findAll("span")[0]
                            .text.split("(")[0]
                            .replace("\n", "")
                            .replace("\t", "")
                            .__contains__("U")
                            and "Under"
                            or "Over",
                            "team": "Total",
                            "spread": list(odd.findAll("tr"))[12]
                            .findAll("span")[0]
                            .text.split("(")[0]
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace("O", "")
                            .replace("U", ""),
                        }
                    )
                case 6:
                    all_odds[index].append(
                        {
                            "sport_league": list(odd.findAll("tr"))[14]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "event_date_utc": list(odd.findAll("tr"))[14]
                            .findAll("span")[1]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team1": list(odd.findAll("tr"))[3]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "team2": list(odd.findAll("tr"))[9]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", ""),
                            "pitcher": "",
                            "period": list(odd.findAll("tr"))[0]
                            .findAll("span")[0]
                            .text.replace("\t", "")
                            .replace("\n", "")
                            .replace("ODDS", ""),
                            "line_type": "moneyline",
                            "price": list(odd.findAll("tr"))[15]
                            .findAll("span")[0]
                            .text.replace("\n", "")
                            .replace("\t", "")
                            .replace("DRAW", ""),
                            "side": "Draw",
                            "team": "Draw",
                            "spread": 0,
                        }
                    )
        index = index + 1

with open("data.json", "w") as f:
    json.dump(all_odds, f)

json_formatted = json.dumps(all_odds, indent=2)
print(json_formatted)
