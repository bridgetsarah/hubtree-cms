# Defined ''
domain_name = ('batman')
account_name = ('jane doe')
account_domain = ('www.batman.com')
account_tel = ('telephone number')
account_email = ('email')

client_account = ('client_account')
client_owner = ('Client_owner')

# Client account

class client_account(object):
    def __init__(self, account_name, account_domain, account_owner, 
    account_tel, account_email, account_type,):
        self.account_name = ('account_name')
        self.account_domain = ('domain_name')
        self.account_owner = ('account_owner')
        self.account_tel = ('account_tel')
        self.account_email = ('account_email')
        self.account_type = ('account_type')
        return(account_name, account_domain, account_owner, account_tel, account_email, account_type)
print( client_account)

# Client (Account owner details)
class client_owner(object):
    def __init__(self, client_firstname, client_lastname):
        self.client_firstname = ('Jane')
        self.client_lastname = ('doe')
        return (client_firstname + client_lastname)
print(client_owner)