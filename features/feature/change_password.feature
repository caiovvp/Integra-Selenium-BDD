  Feature: Change Account Password being logged in

    Scenario: When the user changes password successfully
      Given that I am logged in Integra
      When enters the users page
      And changes the old password
      """
          {
            "password": ["senha", "senha123", "Senha123",  "Senha@123"]
          }
      """
      And try to log in with the new password
      """
          {
            "user": "integra_tester",
            "password": ["Senhas@123", "Senha@123"]
          }
      """
      Then the dashboard page should open