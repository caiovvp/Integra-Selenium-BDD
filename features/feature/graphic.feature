    Feature: Show graphics and info as the dashboard loads

      Scenario: Show all information and Graphic accordingly
        Given user is logged in Integra
        Then show all the integrations information
        And show the integrations graphic

      Scenario: Show graphic according to the filter applied
        #Needs to add validation to the "period" filter on the graphic
        Scenario: Change graphic according to the time filter applied
          When time filter is chosen
          Then show the integrations graphic
        Scenario: Change graphic according to the time filter applied
          When integration filter is chosen
          Then reload the page
          And show the integrations graphic