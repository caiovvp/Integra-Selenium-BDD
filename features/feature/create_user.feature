    Feature: Create user inside Integra

      Background:
        Given that I am logged in Integra
        And enter the users page
        And click on the add new user button

        Scenario: Type existent username
          When type an username that is already registered
          Then show message saying
          """
          {
          "message": "DBException",
          "web_ele": "/html/body/div[1]/h1"
          }
          """

          Scenario: Type existent email
          When type an email that is already registered
          Then show message saying
          """
          {
          "message": "DBException",
          "web_ele": "/html/body/div[1]/h1"
          }
          """

        @kik
        Scenario: User successfully created
          When type all valid infos
          Then show message saying
          """
          {
          "message": "Usuário adicionado com sucesso",
          "web_ele": "/html/body/div[1]/div/div/div/h4"
          }
          """
          And find new user in users page

        @kik
        Scenario: Delete new user
          Given enter the users page
          Then find new user in users page
          When delete new user successfully
          And try to log in with deleted user
          Then show message saying
          """
          {
          "message": "Nome de usuário ou senha incorretos",
          "web_ele": "/html/body/div/div/div[1]/div/form/div[2]"
          }
          """