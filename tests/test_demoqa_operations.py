from demoqa_tests.application import app
from demoqa_tests.data import users


def test_complete_demoqa():
    app.student_reg_form.register(users.admin)
    app.student_reg_form.should_have_registered(users.admin)
