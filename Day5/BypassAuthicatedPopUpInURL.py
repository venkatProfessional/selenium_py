from selenium_helper.common_code import CommonCode

browser5 = CommonCode()


# by passing with the URl
# it wil be bypssed it not showing any alert window
browser5.open_url("http://admin:admin@the-internet.herokuapp.com/basic_auth")

