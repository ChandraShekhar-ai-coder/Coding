code_obj = compile(1/', '', 'exec')
print(type(code_obj))
# <class 'code'>

import dis
dis.dis(code_obj)

