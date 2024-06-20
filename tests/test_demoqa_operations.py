import time
from selene import browser
from conditions import match

def test_complete_demoqa():
    #Тесты
    browser.open("automation-practice-form")
    browser.element('#firstName').type('Petr')
    browser.element('#lastName').type('Andreev')
    browser.element('#userNumber').type('12345678998')
    browser.element('#userEmail').type('for_example@gmail.com')
    browser.element('#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').press("1999").click()
    browser.element('.react-datepicker__month-select [value="4"]').click()
    browser.element('[aria-label="Choose Friday, May 28th, 1999"]').click()
    browser.element('.subjects-auto-complete__input #subjectsInput').type('co').press_enter()
    browser.element('#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label').click()
    browser.element('#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(3) > label').click()
    browser.element('#uploadPicture').send_keys('C:/Users/WS_STO/Desktop/foto.png')
    browser.element('#currentAddress').type('Нижегородская обл, г Выкса')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').press_enter()

    #Проверки
    browser.element('#example-modal-sizes-title-lg').should(match.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(match.exact_texts(
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
