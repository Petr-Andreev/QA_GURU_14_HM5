from selene import browser, have
from demoqa_tests import resource


class PracticeFormPage:

    def __init__(self):
        self.successful_authentication = browser.element('#example-modal-sizes-title-lg')
        self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_checkbox(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        
    def fill_foto(self):
        browser.element('#uploadPicture').set_value(resource.path('foto.png'))
        
    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, name):
        browser.element('#react-select-3-input').type(name).press_enter()

    def fill_city(self, name):
        browser.element('#react-select-4-input').type(name).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()
