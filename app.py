import os
import sys
import time

from screen_manager import ScreenManager

pathImages = os.path.dirname(os.path.realpath(__file__)) + "\images\\"
pathChampionsImages = pathImages + "champions\\"
banChampionText = "Yasuo"
selectChampionText = "Kayn"

def run():
    while True:
        coordinatesAcceptMatch = ScreenManager.search_unique_image_on_screen(image_to_search=pathImages + "AcceptMatch.png")

        coordinatesMessageDeclareChampion = ScreenManager.search_unique_image_on_screen(
            image_to_search=pathImages + "MessageDeclareChampion.png")

        coordinatesMessageBanChampion = ScreenManager.search_unique_image_on_screen(
            image_to_search=pathImages + "MessageBanChampion.png")

        coordinatesMessageSelectChampion = ScreenManager.search_unique_image_on_screen(
            image_to_search=pathImages + "MessageChooseChampion.png")

        if coordinatesAcceptMatch:
            acceptMatch(coordinatesAcceptMatch)

        if coordinatesMessageDeclareChampion:
            selectOrBanChampion(selectChampionText, "Declarei")

        if coordinatesMessageBanChampion:
            selectOrBanChampion(banChampionText, "Bani")

        if coordinatesMessageSelectChampion:
            selectOrBanChampion(selectChampionText, "Selecionei")

def acceptMatch(coordinate: int):
    ScreenManager.click_on_screen(coordenate_to_click=coordinate)
    time.sleep(2)
    print("Aceitei a partida!")

def selectOrBanChampion(champion: str, message: str):
    coordinatesSearchChampion = ScreenManager.search_unique_image_on_screen(image_to_search=pathImages + "SearchChampion.png")
    ScreenManager.click_on_screen(coordenate_to_click=coordinatesSearchChampion)
    time.sleep(2)

    ScreenManager.write(champion)
    time.sleep(3)

    coordinateSelectChampion = ScreenManager.search_unique_image_on_screen(
        image_to_search=pathChampionsImages + champion + ".png")

    ScreenManager.click_on_screen(coordenate_to_click=coordinateSelectChampion)
    time.sleep(2)

    if message != "Bani":
        coordinateBanChampion = ScreenManager.search_unique_image_on_screen(
            image_to_search=pathImages + "ConfirmChampion.png")
        ScreenManager.click_on_screen(coordenate_to_click=coordinateBanChampion)
    else:
        coordinateConfirmChampion = ScreenManager.search_unique_image_on_screen(
            image_to_search=pathImages + "BanChampion.png")
        ScreenManager.click_on_screen(coordenate_to_click=coordinateConfirmChampion)

    time.sleep(2)

    print(f"{message} personagem na partida!")

    if message == "Selecionei":
        sys.exit()

run()