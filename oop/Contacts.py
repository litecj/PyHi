class Contacts (object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        return print(f'name : {self.name} phone : {self.phone} email : {self.email} add : {self.address}  ')

    def to_string2(self):
        return print(f'name : {self.name} \nphone : {self.phone} \nemail : {self.email} \nadd : {self.address}  ')

def set_contact() -> object:
    return Contacts(input('name:'), input('phone:'), input('email:'), input('add:'))

def get_contacts(ls):
    for i in ls:
        i.to_string()
    #input('name:') in Contacts.ls


def del_contact(ls,name):
    for i, j in enumerate(ls):
        if name == j.name:
            del ls[i]
    #contacts.ls.remove(input('name:'))

def pr_menu(ls) -> int:
    #return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))

def main():
    ls = []
    while 1 :
        menu = pr_menu(['exit', 'add', 'print', 'delete'])
        if  menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contacts(ls)
        elif menu == 3:
            del_contact(ls, input('Del Name'))
        else:
            break

if __name__ == '__main__':
    #ls = ['0.exit', '1.add', '2.print', '3.delete']
    #ls2 = ['exit', 'add', 'print', 'delete']
    #print(menu(ls2))
    main()
