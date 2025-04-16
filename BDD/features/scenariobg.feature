Feature: OrangeHRM Login
  Background: Common steps
    Given I launch the browser
    When I open the OrangeHRM application
    And I enter a valid username and password
    And I click on the login button

  Scenario: Login to HRM Application
    Then the user should be redirected to the Dashboard page


  Scenario: Search user
    When navigate to search page
    Then search page showld display

  Scenario: Advance search browser
    When navigate to the advance search page
    Then advance search page showld display
