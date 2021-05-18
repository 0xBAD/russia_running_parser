from selenium import webdriver

URL = "https://russiarunning.com/events?discipline=run"
CHROME_WEBDRIVER_EXECUTABLE_PATH = "/Users/p.gagloev/Downloads/chromedriver"


class RunningRussiaParser:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_EXECUTABLE_PATH)


    def parse_events(self, elements: list):
        res = ""
        for p_element in elements:
            event_date = p_element.find_element_by_class_name("event-card__header-col").text
            card_name = p_element.find_element_by_class_name("event-card__name").text
            event_link = p_element.find_element_by_class_name("event-card__name").get_attribute("href")
            event_location = p_element.find_element_by_class_name("event-card__location").text
            res += f"{event_date}\n{card_name}\n{event_link}\n{event_location}\n\n"
        return res

    def run(self):
        button_num = 1
        self.driver.get(URL)
        pagination_row = self.driver.find_elements_by_class_name("pagination__button")
        for pagination_button in pagination_row:
            if pagination_button.text.isdigit():
                button_num = pagination_button.text
        current_page = 0
        with open("results.txt", "w") as fs:
            while current_page < int(button_num):
                p_elements = self.driver.find_elements_by_class_name("event-card")
                data = self.parse_events(p_elements)
                fs.write(data)
                current_page += 1
                self.driver.get(f"{URL}&p={current_page}")


if __name__ == '__main__':
    parser = RunningRussiaParser()
    parser.run()
