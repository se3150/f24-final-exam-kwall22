Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I set "software quality" to the inputfield "#letters"
    And I click on the element "#shift-amount"
    And I select the option with the value "2" for element "#shift-amount"
    And I click on the element "#submit"
    And I pause for 200ms
    Then I expect that element "#decoded_message" contains the text "uqhvyctg swcnkva"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I set "uqhvyctg swcnkva" to the inputfield "#letters"
    And I select the option with the text "Decode" for element "#decoder-setting"
    And I select the option with the value "2" for element "#shift-amount"
    And I click on the element "#submit"
    And I pause for 300ms
    Then I expect that element "#decoded_message" contains the text "software quality"
