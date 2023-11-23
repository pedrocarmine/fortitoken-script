users_file = open('users.txt', 'r')
users = users_file.readlines()

tokens_file = open('tokens.txt', 'r')

emails_file = open('emails.txt', 'r')

for user in users: # cycle til the last user (last line)
    token = tokens_file.readline().strip() # reads next token
    email = emails_file.readline().strip() # reads nex email

    print(f"edit {user.strip()}")
    print(f"set two-factor fortitoken")
    print(f"set fortitoken {token}")
    print(f"set email-to {email}")
    print("next")