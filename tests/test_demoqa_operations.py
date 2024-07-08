from selene import browser, have

from demoqa_tests import resource


#def resource_path(file_name):
#    str(Path(tests.__file__).paretn.joinpath(f"resources/{file_name}").absolute())


def test_complete_demoqa():
    browser.open("/automation-practice-form")
    browser.element('#firstName').type('Petr')
    browser.element('#lastName').type('Andreev')
    browser.element('#userNumber').type('12345678998')
    browser.element('#userEmail').type('for_example@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').type("1999").click()
    browser.element('.react-datepicker__month-select').element('[value="4"]').click()
    browser.all('.react-datepicker__day--028').second.click()
    browser.element('.subjects-auto-complete__input #subjectsInput').type('co').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(resource.path('foto.png'))
    #browser.element('#uploadPicture').send_keys(os.path.abspath('foto.png'))
    browser.element('#currentAddress').type('Нижегородская обл, г Выкса')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts(
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
                    'Haryana Panipat')
    )
