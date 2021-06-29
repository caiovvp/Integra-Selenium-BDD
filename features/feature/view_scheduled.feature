    Feature: View scheduled processes on the Schedules tab

      Scenario: View scheduled processes successfully
        Given that I am logged in Integra
        When go to the Schedules tab
        And select a schedule
        And click on the view schedule button
        Then show the list of processes found in that schedule

#      Scenario: Empty schedule....
#        Given
#        When
#        Then