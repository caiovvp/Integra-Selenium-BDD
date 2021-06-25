 Feature: Change account password

    Background:
    Given that I am on the login page
    And click on the change password button
      Scenario: Account email exists
        When type a valid email on the email box
        And click on the request new password button
        Then a message saying that the verification Code was sent is shown
          """
          {"msg_valid_email": "Código enviado. Verifique seu e-mail."}
          """

      Scenario: Account email doesnt exist
        When type an invalid email on the email box
        And click on the request new password button
        Then a message saying that no account is linked to that email is shown
          """
          {"msg_invalid_email": "Não há nenhum usuário com esse email"}
          """
