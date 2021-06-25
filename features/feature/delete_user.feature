 Feature: Change account password

    Background:
    Given that I am logged in Integra
    And enter the users page
      Scenario:
        When
        And
          """
          {"msg_valid_email": "Código enviado. Verifique seu e-mail."}
          """

      Scenario: Account email doesnt exist
        When
        And
        Then
          """
          {"msg_invalid_email": "Não há nenhum usuário com esse email"}
          """
