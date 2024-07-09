from selene import browser, have
from demoqa_tests import resource
from demoqa_tests.pages.registration_page import RegistrationFormPage


def test_complete_demoqa():
    registration_page = RegistrationFormPage()
    # open registration form
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Petr')

    #Доделать
    # browser.element('#lastName').type('Andreev')
    # browser.element('#userNumber').type('12345678998')
    # browser.element('#userEmail').type('for_example@gmail.com')
    # browser.element('[for="gender-radio-1"]').click()

    registration_page.fill_birthday('1999', 'May', '28')

    #Доделать
    # browser.element('#subjectsInput').type('Computer Science').press_enter()
    # browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    # browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()
    # browser.element('#uploadPicture').set_value(resource.path('foto.png'))
    # browser.element('#currentAddress').type('Нижегородская обл, г Выкса')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')
    # Доделать
    # browser.element('#submit').press_enter()

    #THEN
    # Доделать
    # browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    registration_page.registered_user_data.should(
        have.exact_texts(
        'Petr Andreev',
        'for_example@gmail.com',
        'Male',
        '1234567899',
        '28 May,1999',
        'Computer Science',
        'Sports, Music',
        'foto.png',
        'Нижегородская обл,'
        ' г Выкса',
        'Haryana Panipat'
        )
    )
