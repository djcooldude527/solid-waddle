file_name = 'journal.txt'
content_to_append = f'{input('New entry:\n')}\n'

try:
    with open(file_name, 'a') as f:
        f.write(content_to_append)
    print(f"Journal entry added!")
except IOError as e:
    print(f"Error: Could not open or write to journal somehow... Python said: {e}")
quit