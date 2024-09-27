def send_email(message, recipient, sender="university.help@gmail.com"):
    if ("@" not in sender or "@" not in recipient
            or not (sender.endswith((".com", ".ru", ".net")))
            or not (recipient.endswith((".com", ".ru", ".net")))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Привет!", "recipient@example.com")
send_email("Привет!", "recipient@example.com", "custom.sender@mail.com")
send_email("Привет!", "university.help@gmail.com")
send_email("Привет!", "invalid_email")