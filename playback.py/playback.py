initial_prompt=input("Enter your prompt!").strip()
new_list=initial_prompt.split()
new=''
for char in new_list:
    new +=char + '...'

print(new.strip('...'))
#Successfully solved. 
