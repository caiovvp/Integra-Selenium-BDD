    Feature: Login on the website

      Scenario: Account exists
        Given that I am on the login page
        When type valid credentials
          """
            {
              "user": "integra_tester",
              "password": "Senha@123"
            }
          """
        Then the dashboard page should open

      Scenario: Account doesnt exist
        Given that I am on the login page
        When type invalid credentials
          """
            {
              "user": ["integra_tester", "integra_xxx"],
              "password": ["Senha@123xxx", "Senha@123"]
            }
          """
        Then the website should show an error message saying invalid user or password
          """
            {"msg_error": "Nome de usuário ou senha incorretos"}
          """