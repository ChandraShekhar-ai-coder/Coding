code_obj = compile('x = a+ b', '', 'exec')
print(type(code_obj))
# <class 'code'>

import dis
dis.dis(code_obj)

1/0