record = ("Peter", "Peter@example", "010", "020")

name, email, *phone_numbers = record

print(phone_numbers)

passwd = "root:x:0:0:root:/root:/bin/bash"

user, *fields, home_dir, sh = passwd.split(":")

print(fields)
