greeting = "Hello World! "
today = "This is a really good day!"

todays_greeting = greeting + today
print("\n" + todays_greeting)

haiku = "\nThis is the beginning\nof this bootcamp\nI pray that I continue to\nunderstand everything"
print(haiku)

person = "Kevin"
today = "Tuesday"
emotion = "happy"

first_paragraph = f'''
Hello {person},
I hope that your {today} is going well.
I'm personally really {emotion}!
'''

second_paragraph = '''
Hello %s,
I hope that your %s is going well.
I'm personally really %s!
'''

third_paragraph='''
Hello {},
I hope that your {} is going well.
I'm personally really {}!\n
'''.format(person, today, emotion)
print(first_paragraph ,second_paragraph % (person, today, emotion), third_paragraph)
