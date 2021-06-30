    Feature: View executions of all processes

      Background: Log in Integra and go to Executions
        Given user is logged in Integra
        And go to the Executions tab

        Scenario: View all the integrations
          When go to all processes
          Then show the all the executions of all processes


        Scenario: View executions of each process
          When open list of processes
          And select a process of the list
          Then show a list of all executions on that process