Feature: dividing two numbers
  
  Scenario: when dividing two nonzero integers
    Given two valid integers
    When dividing the integers
    Then it should result to another integer
  
  Scenario: when dividing zero with zero
    Given two integers are zero
    When dividing the integers
    Then it should result to zero
    
  Scenario: when dividing a nonzero integer with zero
    Given one integer is nonzero and one integer is zero
    When dividing the integers
    Then it should result to zero