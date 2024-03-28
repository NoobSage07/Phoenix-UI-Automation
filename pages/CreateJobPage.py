import time
from pages.BasePage import BasePage


class CreateJobPage(BasePage):
    # Device Details Locators
    oem_LOCATOR_XPATH = "//mat-select[@placeholder='Select OEM']"
    product_XPATH = "//span[contains(text(),'Select Product name')]"
    model_XPATH = "//span[contains(text(),'Select Model name')]"
    imei_XPATH = "//input[@formcontrolname='imeiNo1']"
    date_XPATH = "//input[@data-placeholder='dd/mm/yyyy']"
    warranty_XPATH = "//span[contains(text(),'Select Warranty Status')]"

    # PROBLEM DETAIL
    problem_XPATH = "//mat-select[@placeholder='Select Problem']"
    remarks_XPATH = "//input[@data-placeholder='Remarks']"

    # CUSTOMER DETAILS
    firstName_XPATH = "//input[@data-placeholder='First Name']"
    lastName_XPATH = "//input[@data-placeholder='Last Name']"
    contactNO_XPATH = "//input[@data-placeholder='Contact No.']"
    email_XPATH = "//input[@data-placeholder='Email Id.']"
    flat_XPATH = "//input[@data-placeholder='Flat/Society No.']"
    apartment_XPATH = "//input[@data-placeholder=\"Apartment Name\"]"
    landmark_XPATH = "//input[@data-placeholder='Choose a Landmark']"
    streetName_XPATH = "//input[@data-placeholder='Street Name.']"
    area_XPATH = "//input[@data-placeholder='Area']"
    state_XPATH = "//input[@data-placeholder='Select State']"
    pincode_XPATH = "//input[@data-placeholder='Pincode']"

    # Button Action
    clearField_XPATH = "//span[contains(text(),' Clear ' )]/../../button[1]"
    submit_XPATH = "//span[contains(text(),' Submit ' )]/../../button[2]"

    def __init__(self, driver):
        super().__init__(driver)

    def selectOEM(self, oem_TEXT):
        self.element_click("oem_LOCATOR_XPATH", self.oem_LOCATOR_XPATH)
        time.sleep(1)
        # Construct the dynamic locator for the option
        oem_dynamic__XPATH = f"//span[contains(text(), '{oem_TEXT}')]"
        self.element_click("oem_dynamic__XPATH", oem_dynamic__XPATH)
        return self

    def selectProductName(self, product_TEXT):
        self.element_click("product_XPATH", self.product_XPATH)
        time.sleep(1)
        product_dynamic_XPATH = f"//span[contains(text(), '{product_TEXT}')]"
        self.element_click("product_dynamic_XPATH", product_dynamic_XPATH)
        return self

    def selectModelName(self, model_TEXT):
        self.element_click("model_XPATH", self.model_XPATH)
        time.sleep(1)
        # Construct the dynamic locator for the option
        model_dynamic_XPATH = f"//span[contains(text(), '{model_TEXT}')]"
        self.element_click("model_dynamic_XPATH", model_dynamic_XPATH)
        return self

    def enterIMEI(self, imei_TEXT):
        self.type_into_element(imei_TEXT, "imei_XPATH", self.imei_XPATH)
        time.sleep(1)
        return self

    def enterDateOfPurchase(self, date_TEXT):
        self.type_into_element(date_TEXT, "date_XPATH", self.date_XPATH)
        return self

    def selectInWarrantyStatus(self, inWarranty_TEXT):
        self.element_click("warranty_XPATH", self.warranty_XPATH)
        time.sleep(2)
        inWarranty_dynamic_XPATH = f"//span[contains(text(), '{inWarranty_TEXT}')]"
        self.element_click("inWarranty_dynamic_XPATH", inWarranty_dynamic_XPATH)
        return self

    def selectProblem(self, problem_TEXT):
        self.element_click("problem_XPATH", self.problem_XPATH)
        time.sleep(2)
        problem_dynamic_XPATH = f"//span[contains(text(), '{problem_TEXT}')]"
        self.element_click("problem_dynamic_XPATH", problem_dynamic_XPATH)
        return self

    def enterRemarks(self, remarks_TEXT):
        self.type_into_element(remarks_TEXT, "remarks_XPATH", self.remarks_XPATH)
        return self

    def enterFirstName(self, firstName_TEXT):
        self.type_into_element(firstName_TEXT, "firstName_XPATH", self.firstName_XPATH)
        return self

    def enterLastName(self, lastName_TEXT):
        self.type_into_element(lastName_TEXT, "lastName_XPATH", self.lastName_XPATH)
        return self

    def enterContactNo(self, contactNo_TEXT):
        self.type_into_element(contactNo_TEXT, "contactNO_XPATH", self.contactNO_XPATH)
        return self

    def enterEmail(self, email_TEXT):
        self.type_into_element(email_TEXT, "email_XPATH", self.email_XPATH)
        return self

    def enterFlatNo(self, flatNo_TEXT):
        self.type_into_element(flatNo_TEXT, "flat_XPATH", self.flat_XPATH)
        return self

    def enterApartmentNo(self, apartmentNo_TEXT):
        self.type_into_element(apartmentNo_TEXT, "apartment_XPATH", self.apartment_XPATH)
        return self

    def enterLandmark(self, landmark_TEXT):
        self.type_into_element(landmark_TEXT, "landmark_XPATH", self.landmark_XPATH)
        return self

    def enterStreetName(self, streetName_TEXT):
        self.type_into_element(streetName_TEXT, "streetName_XPATH", self.streetName_XPATH)
        return self

    def enterArea(self, area_TEXT):
        self.type_into_element(area_TEXT, "area_XPATH", self.area_XPATH)
        return self

    def selectState(self, state_TEXT):
        self.element_click("state_XPATH", self.state_XPATH)
        time.sleep(2)
        state_dynamic_XPATH = f"//span[contains(text(), '{state_TEXT}')]"
        self.element_click("state_dynamic_XPATH", state_dynamic_XPATH)
        return self

    def enterPincode(self, pincode_TEXT):
        self.type_into_element(pincode_TEXT, "pincode_XPATH", self.pincode_XPATH)
        return self

    def clearJobFields(self):
        self.element_click("clearField_XPATH", self.clearField_XPATH)

    def submitJob(self):
        self.element_click("submit_XPATH", self.submit_XPATH)
