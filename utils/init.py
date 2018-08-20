import os
import shutil
import HTML

print('Resetting kernel environmental variables ...') 
shutil.move(os.path.join(os.getcwd(), 'utils', 'init.py'),
            os.path.join(os.getcwd(), '.ipython', 'profile_default', 'startup', 'init.py'))
print(html.unescape("Kernel environment variables reset. Please press '&#8635;' above or '0' on your keyboard"))
