Feature: Search in Sogou website
  In order to Search in Sogou  website
  As a visitor
  We'll search the NBA best player

  Scenario: Search NBA player
    Given I have the english name "<search_name>"
    When  I search it in Sogou website
    Then  I see the entire name "<search_result>"

  Examples:
    | search_name | search_result |
    | Jordan      | Michael       |
    | Curry       | Stephen       |
    | Kobe        | Bryant        |
