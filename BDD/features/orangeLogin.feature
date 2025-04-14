Feature: orangeHRM Login
  Scenario: login to orangeHRM with valid parameters
    Given i launch the chrome browser
    When i open orangeHRM home page
    And  Enter username "Admin" and password "admin123"
    And  Click login button
    Then User successfully loged in

  Scenario Outline: login with multiple credentials
    Given i launch the chrome browser
    When i open orangeHRM home page
    And Enter username "<username>" and password "<password>"
    And  Click login button
    Then User successfully loged in

    Examples:
       |username|password|
       |Admin|admin123|
       |admin123|admin1|
       |admin|admin|



