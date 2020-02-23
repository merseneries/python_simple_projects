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
            print(f"{key}:{value}")
        print("-"*40)


if __name__ == '__main__':
    email_list = ["bondps@bonansatours.com", "baliprestigeho@dps.centrin.net.id", "witamgr@dps.centrin.net.id",
                  "indahsuluh2002@yahoo.com.sg", "imz1991@yahoo.com"]
    print_email(split_email(email_list))
