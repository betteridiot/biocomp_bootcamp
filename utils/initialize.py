import os
import shutil
import html

print('Resetting kernel environmental variables ...') 
try:
    shutil.move(os.path.join(os.getcwd(), 'utils', 'init.py'),
                os.path.join(os.getcwd(), '.ipython', 'profile_default', 'startup', 'init.py'))
    print(html.unescape("Kernel environment variables reset. Please press '&#8635;' above or '0' on your keyboard"))
except FileNotFoundError:
    if os.path.isfile(os.path.join(os.getcwd(), '.ipython', 'profile_default', 'startup', 'init.py')):
        if os.getenv('CULL_TIMEOUT') == '28800':
            print('Kernel environmental variables already set. Please continue.')
        else:
            print(html.unescape("Kernel environment variables already reset. Please press '&#8635;' above or '0' on your keyboard"))

