from selene import browser, have, be
from demoqa_tests import resource
from demoqa_tests.data.users import User


class PracticeFormPage:

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

    def fill_gender(self, name):
        browser.element(f'[name=gender][value={name}]+label').click()

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

    def fill_foto(self, file_name):
        browser.element('#uploadPicture').set_value(resource.path(f'{file_name}'))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, name):
        browser.element('#react-select-3-input').type(name).press_enter()

    def fill_city(self, name):
        browser.element('#react-select-4-input').type(name).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def register(self, admin: User):
        self.fill_first_name(admin.first_name)
        self.fill_last_name(admin.last_name)
        self.fill_user_number(admin.mobile)
        self.fill_user_email(admin.email)
        self.fill_gender(admin.gender)
        self.fill_birthday(admin.year_of_birth, admin.month_of_birth, admin.day_of_birth)
        self.fill_subjects(admin.subjects)
        self.fill_checkbox(admin.hobbies)
        self.fill_checkbox(admin.hobbies_two)
        self.fill_foto(admin.photo)
        self.fill_address(admin.address)
        self.fill_state(admin.state)
        self.fill_city(admin.city)
        self.submit()

    def should_have_registered(self, admin: User):
        browser.element('#example-modal-sizes-title-lg').should(be.present)
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{admin.first_name} {admin.last_name}',
            f'{admin.email}',
            f'{admin.gender}',
            f'{admin.mobile}',
            f'{admin.day_of_birth} {admin.month_of_birth},{admin.year_of_birth}',
            f'{admin.subjects}',
            f'{admin.hobbies}, {admin.hobbies_two}',
            f'{admin.photo}',
            f'{admin.address}',
            f'{admin.state} {admin.city}'
        ))
