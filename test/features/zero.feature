Feature: Compute sum
  In order to play with Lettuce
  As beginners
  We'll implement sum

  Scenario: sum of 1,2
    Given I have the number 1,2
    When I compute its sum
    Then I see the number 3

