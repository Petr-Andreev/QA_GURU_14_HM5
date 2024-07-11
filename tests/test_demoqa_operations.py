from demoqa_tests.application import app
from demoqa_tests.data import users


def test_complete_demoqa():
    app.left_panel.open()
    app.left_panel.register(users.admin)
    app.left_panel.should_have_registered(users.admin)
