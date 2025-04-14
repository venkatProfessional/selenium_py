Feature: OrangeHRM logo
  Scenario: logo presence on Orange HRM home page
    Given launch chorme browser
    When  open orange HRM home page
    Then  verify the logo presence or not
    And   close Browser

