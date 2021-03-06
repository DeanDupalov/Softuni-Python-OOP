class EmailValidator:
    min_length: int
    mails: list
    domains: list

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    @staticmethod
    def __get_name_mail_domain(email):
        name = email[:list(email).index('@')]
        mail = email[list(email).index('@') + 1:list(email).index('.')]
        domain = email[list(email).index('.') + 1:]
        return name, mail, domain

    def validate(self, email):
        name, mail, domain = self.__get_name_mail_domain(email)
        return all([self.__validate_name(name), self.__validate_mail(mail), self.__validate_domain(domain)])


