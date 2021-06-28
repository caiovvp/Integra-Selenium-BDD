 Feature: Delete user

    Background: Create new user to be deleted
    Given that I am logged in Integra
    And enter the users page
    And click on the add new user button
    When type all valid infos
    Then show message saying
      """
      {
      "message": "Usuário adicionado com sucesso",
      "web_ele": "/html/body/div[1]/div/div/div/h4"
      }
      """
      Scenario: New user deleted successfully
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

