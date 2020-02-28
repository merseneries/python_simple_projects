import re


def split_email(emails):
    emails = [emails] if type(emails) == str else emails
    all_emails = []

    for i in emails:
        tmp = i.split("@")
        email_dict = {"username": tmp[0], "domains": tmp[1].split(".")}
        all_emails.append(email_dict)

    return all_emails


def print_email(email):
    for dic in email:
        for key, value in dic.items():
            print(f"{key}: {value}")
        print("-" * 40)


def check_valid_email(email_text):
    return bool(re.search(r"[a-zA-Z0-9]{4,}@([a-zA-Z0-9]{2,}\.){1,4}[a-zA-Z0-9]{2,3}", email_text))


if __name__ == '__main__':
    input_email = input("Input email to split: ")
    if check_valid_email(input_email):
        print_email(split_email(input_email))
    else:
        print("Invalid email. Email can contain: a-z, A-Z, 0-9 and '.'\nExample: gronioman@gmail.com")