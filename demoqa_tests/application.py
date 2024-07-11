from demoqa_tests.pages.registration_page import PracticeFormPage
from demoqa_tests.pages.text_box_page import TextBoxFrom


class Application:
    def __init__(self):
        self.text_box_form = TextBoxFrom()
        self.left_panel = PracticeFormPage()


app = Application()
