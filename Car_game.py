#!/usr/bin/env python
# coding: utf-8

# In[10]:


command=''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
    elif command == 'stop':
        if not started:
            print("Car is already stopped.")
        else:
            started = False
    elif command == 'help':
        print(""" 
start - to start the car
stop - to stop the car
quit - to quit
""")
    elif command == 'quit':
        break
    else:
        print('Sorry, I do not understand that!')


# In[ ]:




