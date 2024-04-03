# Using regex with Python scripts
# a+ matches a, aaa, aaaaaaaaaaaaaaa
# \w matches 1, k, i, no symbols
# user1@email1.com, \w+@\w+\.\w+
import re
email_log = """Email received June 2 from user1@email.com.
            Email received June 2 from user2@email.com
            Email received June 2 from invalid_email@email.com"""

print(re.findall("\w+@\w+\.\w+",email_log))