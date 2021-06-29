    Feature: View scheduled processes on the Schedules tab

      Scenario: View scheduled processes successfully
        Given user is logged in Integra
        When go to the Schedules tab
        And select each schedule and click on the button
        Then show the list of processes found in that schedule
