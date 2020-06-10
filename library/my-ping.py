#!/bin/env python3

#This is a Python code to create a custom Ansible module 
#Create a directory name library/ where you have your plabooks and then create a python file in the library directory and give it a name that you want to call your module
#We begin by cloning the  repository here : git clone https://github.com/ansible/ansible.git
#This will automatically make available the AnsibleModule to this Python script; which will be supplied by the ansible.module.utils.basic module.
from ansible.module_utils.basic import AnsibleModule

#The rest of the modules imported below depends on your need in writing your code.
import os
import sys
import json

def my_module():
        #Here I am invoking the AnsibleModule and storing it in the module variable, while at the same time passing its arguments to it.
	module=AnsibleModule(
                        #Here I am defining module arguments that I will use for my module, just like you pass options to a command on a command line 
			argument_spec=dict(
				filename=dict(type='str', required=True),  
                                another_argument=dict(type='bool', required=False)
			),
                        #Here I am invoking the check-mode option of ansible and setting it to True. Meaning that I can the module on check mode only.
			supports_check_mode=True


	)
        #Here I am defining what information I want returned from managed nodes after a successful chage of state on the nodes.
	result = dict(
		changed=True,
		original_message='Playbook ran successfully',
		message='The state of remote hosts changed'
	)
        #This is where my normal Python code  is written. Here I invoke my module's arguments defined above inside my Python code with the module.params method.
        #Write your code just like you would in a normal python code, use whatever logic you want here.
        #os.system('touch {}'.format(module.params['filename']))
        
	#In the code above, I am creating a file. In the playbook, I will enter the name of this python script file in place of module name and the option will be filename.
        #EXAMPLE:
        # - name: Creating a file
        #   my_own_module_name:
        #        filename: 'enter the file I want to create here'
        #        another_argument: False
        

        #Here I am telling ansible to exit while returning information from manages nodes to the ansible control node. This is what you see displayed on the screen after a successful run
        #module.exit_json(**result)

        #Here I am conditioning the playbook to run if not in check mode. So if I append --check to the ansible-plabook command the play will run in check mode, else it will change state
	if not module.check_mode:
		os.system('touch {}'.format(module.params['filename']))
        module.exit_json(message='running in check mode')

#Here I am simply calling the function above with another function
def main():
	my_module()

if __name__ == '__main__':
    main()
    



