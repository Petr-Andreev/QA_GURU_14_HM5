from selene import browser, have, be, command

from demoqa_tests.data.users import UserTextBox


class TextBoxFrom:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout=10).wait_until(have.size_greater_than_or_equal(3)
                                   )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.driver.execute_script('document.querySelector(".body-height").style.transform = "scale(.90)"')

    def open_simple_registration_form(self, text_box_from=None):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout=10).wait_until(have.size_greater_than_or_equal(3)
                                   )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.all('.element-group').first.should(have.text('Elements')).click()
        browser.all('.menu-list .text').element_by(have.exact_text('Text Box')).click()
        return text_box_from

    def fill_full_name(self, value):
        browser.element('#userName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_current_address(self, current_address):
        browser.element('#currentAddress').type(current_address).press_enter()
        return self

    def fill_permanent_address(self, permanent_address):
        browser.element('#permanentAddress').type(permanent_address).press_enter()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def register_text_box(self, user: UserTextBox):
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.fill_current_address(user.current_address)
        self.fill_permanent_address(user.permanent_address)
        self.submit()
        return self

    def should_text_box_have_registered(self, user: UserTextBox):
        browser.element('#output').should(have.exact_text(f'Name:{user.full_name}\n'
                                                          f'Email:{user.email}\n'
                                                          f'Current Address :{user.current_address}\n'
                                                          f'Permananet Address :{user.permanent_address}'))
        return self
