if __name__ == '__main__':
    
    input = input("Please enter your email: ").strip()
    if '@' in input.lower():
        mail_components = input.split('@')
        print("Your username is:",mail_components[0],"Your domain is:",mail_components[1])
    else:
        print("This is the wrong format for an email!")
