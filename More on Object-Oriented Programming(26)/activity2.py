class employee:
    def __init__(self):
        print('employee created')
    def __init__(self):
        print('destrcutor created')
def create_obj():
    print('making object..')
    obj = employee()
    print('function end...')
    return obj
print('calling create_obj() function....')
obj = create_obj()
print('program End...')