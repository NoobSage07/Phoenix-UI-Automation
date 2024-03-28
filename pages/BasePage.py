from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def press_enter_key(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(Keys.ENTER)

    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_ID"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_NAME"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_CLASS_NAME"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_LINK_TEXT"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_table_values(self, locator_name, locator_value, row_tag_name, cell_tag_name):
        table_values = []

        # Get the table element
        table = self.get_element(locator_name, locator_value)

        # Get all rows of the table
        rows = table.find_elements(By.TAG_NAME, row_tag_name)  # "mat-row"

        # Iterate over each row
        for row in rows:
            # Get all cells of the row
            cells = row.find_elements(By.TAG_NAME, cell_tag_name)  # mat-cell

            # Initialize an empty list to store cell texts
            cell_texts = []

            # Iterate over each cell
            for cell in cells:
                # Retrieve text from the cell
                cell_text = cell.text.strip()

                # Add cell text to the list
                cell_texts.append(cell_text)

            # Append cell texts to the table_values list
            table_values.append(cell_texts)

        for row in table_values:
            print("\t".join("{:<20}".format(cell) for cell in row))
        return table_values
