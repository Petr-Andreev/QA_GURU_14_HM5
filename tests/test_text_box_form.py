from demoqa_tests.application import app
from demoqa_tests.data import users


def test_complete_demoqa():
    app.left_panel.open_text_box_form()
    app.text_box_form.register_text_box(users.user_for_text_box)
    app.text_box_form.should_text_box_have_registered(users.user_for_text_box)
