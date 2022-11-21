import optparse
import re

"""
This program will allow you to slice email into username and domain
There are 3 option available how to do that:
1) you change list of emails in your program (which is called list_emails)
2) before starting your program you can enter -t or --text and past your email 
directly into the terminal to get info, for example:
python3 main.py --text bob@gmail.com
3) before starting your program you can enter -f or --file and past your file 
with emails directly into the terminal to get info, for example:
python3 main.py -f emails.txt
"""


# Creating main class with default attributes
class EmailSlicer:
    counter = 0
    list_emails = ["davydenko_vladyslav@gmail.com", "c308@elint.com.ua", "nazarzuhan454@yahoo.ua", "rererere"]

    def __init__(self) -> None:
        self.user_domain = {}

    # Class method to count the number of emails
    @classmethod
    def add_to_counter(cls):
        cls.counter += 1

    # Main method of program where emails are devided by Regular Expression
    def email_slicer(self):
        pattern = r"(.*)(?:@)(.*)"
        emails = self.start()
        for email in emails:
            username, domain = None, None
            try:
                username = re.search(pattern, email).group(1)
                domain = re.search(pattern, email).group(2)
            except AttributeError:
                pass
            self.user_domain[username] = domain
        return self.user_domain

    # Method which displays all info into terminal
    def get_info(self):
        for name, domain in self.email_slicer().items():
            self.add_to_counter()
            if name and domain and "." in domain:
                print(f"\n{self.counter}) ")
                print(f"Username -> {name}")
                print(f"Domain name -> {domain}")
            else:
                print(f"\n{self.counter}) ")
                print("[-] Invalid email")
    
    # Method that captures info from file and store it into variable 
    def get_info_from_file(self, file):
        try:
            with open(file) as f:
                lines = f.readlines()
                word_list = [line.rstrip() for line in lines]
                return word_list
        except FileNotFoundError:
            print("[-] Cannot open the file")
            return []

    # Method that decide what option will be used
    def start(self):
        """
        Using library optparse to get info from terminal
        so that understand what user wants 
        """
        parser = optparse.OptionParser()
        parser.add_option("-t", "--text", dest="text", help="Enter your email to get info")
        parser.add_option("-f", "--file", dest="file_name", help="Enter file with emails")
        (options, arguments) = parser.parse_args()
        if options.text:
            return [str(options.text)]
        elif options.file_name:
            return self.get_info_from_file(str(options.file_name))
        else:
            return self.list_emails


test = EmailSlicer()
test.get_info()