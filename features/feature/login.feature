  Feature: Login on the website

    Background:
      Given that I am on the login page

      Scenario: Account exists
        When type credentials
          """
            {
              "user": ["integra_tester"],
              "password": ["Senha@123"]
            }
          """
        Then the dashboard page should open

      Scenario: Account doesn't exist
        When type credentials
          """
            {
              "user": ["integra_tester", "integra_xxx", "integra_xxx"],
              "password": ["Senha@123xxx", "Senha@123", "integra_xxx"]
            }
          """
        Then show message saying
          """
            {
              "message": "Nome de usuário ou senha incorretos",
              "web_ele": "/html/body/div/div/div[1]/div/form/div[2]"
            }
          """