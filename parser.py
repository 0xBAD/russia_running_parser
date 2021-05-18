from selenium import webdriver

URL = "https://russiarunning.com/events?discipline=run"
CHROME_WEBDRIVER_EXECUTABLE_PATH = "/Users/p.gagloev/Downloads/chromedriver"


class RunningRussiaParser:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_EXECUTABLE_PATH)


    def parse_events(self, elements: list):
        for p_element in elements:
            # print(p_element.text, end="\n"*2)
            print(p_element.find_element_by_class_name("event-card__header-col").text)
            print(p_element.find_element_by_class_name("event-card__name").text)
            print(p_element.find_element_by_class_name("event-card__name").get_attribute("href"))
            print(p_element.find_element_by_class_name("event-card__location").text, end="\n" * 2)

    def run(self):
        button_num = 1
        self.driver.get(URL)
        pagination_row = self.driver.find_elements_by_class_name("pagination__button")
        for pagination_button in pagination_row:
            if pagination_button.text.isdigit():
                button_num = pagination_button.text
        current_page = 0
        print(button_num)

        while current_page < int(button_num):
            p_elements = self.driver.find_elements_by_class_name("event-card")
            self.parse_events(p_elements)
            current_page += 1
            self.driver.get(f"{URL}&p={current_page}")


if __name__ == '__main__':
    parser = RunningRussiaParser()
    parser.run()
