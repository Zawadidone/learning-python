from re import search

def new_password(oldpassword, newpassword):
	if oldpassword != newpassword and len(newpassword) >= 6 and bool(search(r'\d', newpassword)):
		return True
	else:
		return False


print(new_password("aaaaaaaaaaaa", "111aaaaaaaaaa"))
