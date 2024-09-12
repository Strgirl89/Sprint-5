from faker import Faker

def get_sign_up_data():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    return email, password
def get_sign_up_name_data():
    fake = Faker()
    name = fake.name
    return name

valid_user_data = {
    "email": "adelbatalova@gmail.com",
    "password": "NISSAN1989"
}

class Link:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    LOGIN_URL = f"{BASE_URL}login"
    SIGNUP_URL = f"{BASE_URL}signup"
    ACCOUNT_URL = f"{BASE_URL}account"
    PROFILE_URL = f"{BASE_URL}account/profile"
    REGISTER_URL = f"{BASE_URL}register"

