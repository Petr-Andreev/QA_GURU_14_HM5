from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import PracticeFormPage


def test_complete_demoqa():
    registration_form = PracticeFormPage()
    admin = users.admin
    registration_form.open()
    registration_form.register(admin)
    registration_form.should_have_registered(admin)
