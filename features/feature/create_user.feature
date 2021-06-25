    Feature: Create user inside Integra

      Background:
        Given that I am logged in Integra
        And enter the users page
        And click on the add new user button

        Scenario: User type existent username
          When type an username that is already registered
          Then show message saying:
          """
          {"message": "Username already exists, please choose another one"}
          """

          Scenario: User type existent email
          When type an email that is already registered
          Then show message saying:
          """
          {"message": "Username already exists, please choose another one"}
          """

        Scenario: User type different passwords
          When user type different passwords on the boxes
          Then show message saying:
          """
          {"message": "Username already exists, please choose another one"}
          """

        Scenario: User successfully created
          When user type all valid infos
          Then show message saying:
          """
          {"message": "User successfully created"}
          """
