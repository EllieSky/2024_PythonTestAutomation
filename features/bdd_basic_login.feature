Feature: Basic BDD Login

  Scenario: As an Admin I should be able to login
    Given the page url contains /auth/login
    When I enter text admin into the element id=txtUsername
    And I enter text password into the element id=txtPassword
    And I click the id=btnLogin element
    Then the url should contain /pim/viewEmployeeList
    When I get the text from element id=welcome
    Then the text should be Welcome Admin



  Scenario: Using POM, as an Admin I should be able to login
    Given I authenticate as Admin
    When I authenticate successfully
    Then the welcome message should be Welcome Admin
    And the header should be Employee List