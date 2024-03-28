import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
url = "http://phoenix.testautomationacademy.in/sign-in"
driver.get(url)
# username
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "username").send_keys("iamfd")
# password
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("password")
# SignButton
driver.find_element(By.XPATH, "//span[contains(text(), ' Sign in ')]/../..").click()
time.sleep(4)

# DASHBOARD
dashboard_menu_LOCATOR = "//span[contains(text(), \" Dashboard \")]"
pending_4_delivery_LOCATOR = "//div[contains(text(), \"Pending for delivery\")]/../div/button"
created_today_LOCATOR = "//div[contains(text(),'Created today')]/../div/button"
pending_4_FST_assignment_LOCATOR = "//div[contains(text(),'Pending for FST assignment')]/../div/button"
Download_div = "//a[@href='/frontdesk/download-delivery-note']"
search_field_XPATH = "//input[@data-placeholder='Search Job']"
submit_button_XPATH = "//span[contains(text(),' Submit ')]/.."
signButton_XPATH = "//span[contains(text(), ' Submit ')]/../."

# Printing Table
table_LOCATOR = "//mat-table"
row_LOCATOR = "//mat-header-row"
cell_LOCATOR = "//mat-cell"

# Click on Pending on Delivery
driver.find_element(By.XPATH, Download_div).click()
driver.find_element(By.XPATH, search_field_XPATH).send_keys("JOB_28957")
driver.find_element(By.XPATH, signButton_XPATH).click()
time.sleep(4)
# Locate the table element
table = driver.find_element(By.TAG_NAME, "table")

# Initialize an empty list to store table values
table_values = []

# Get all rows of the table
rows = table.find_elements(By.TAG_NAME, "tr")

# Iterate over each row
for row in rows:
    # Get all cells of the row
    cells = row.find_elements(By.TAG_NAME, "td")

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

# Print table values
for row in table_values:
    print("\t".join(row))
