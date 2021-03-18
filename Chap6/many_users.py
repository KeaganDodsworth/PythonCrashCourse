users = {
'aeinstein': {
				'first': 'albert',
				'last': 'einstein',
				'location': 'princeton',
			 },
'mcurie': {
				'first': 'marie',
				'last': 'curie',
				'location': 'paris',
			},
}


for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

Students = {
'kdodsworth': {
				'first_name': 'keagan',
				'last_name': 'dodsworth',
				'second_name': 'troy',
			 },
'gpalmarozza': {
				'first_name': 'gianluca',
				'last_name': 'palmarozza',
				'second_name': 'squanchy',
			},
}

for student_code, student_info in Students.items():
	print(f"\nStudent code: {student_code}")
	full_name = f"{student_info['first_name']} {student_info['second_name']} {student_info['last_name']}"
	print(f"\tFull name: {full_name.title()}")
	

