import dataclasses

import resource


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    gender: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: str
    hobbies: str
    hobbies_two: str
    photo: str
    address: str
    state: str
    city: str


admin = User(first_name='Petr', last_name='Andreev', email='for_example@gmail.com',
             mobile='1234567899', gender='Male', year_of_birth='1999', month_of_birth='May', day_of_birth='28',
             subjects='Computer Science', hobbies='Sports', hobbies_two='Music',
             address='Нижегородская обл, г Выкса', state='Haryana', city='Panipat', photo='foto.png')
