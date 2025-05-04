import Pyro4

class  StringConcatenator:
    @Pyro4.expose
    def concatenate(self,str1,str2):
        return str1+str2
    
def start_sever():
    conacatenator =StringConcatenator()

    daemon = Pyro4.Daemon()
    url = daemon.register(conacatenator)

    print("Server URL: ",url)

    print("Server is ready.")
    daemon.requestLoop()


if __name__ == '__main__':
    start_sever()



import Pyro4

def main():
    url = input("Enter server's url: ")

    concatenator = Pyro4.Proxy(url)

    str1 = input("Enter string 1: ")
    str2 = input("enter string 2: ")

    result = concatenator.concatenate(str1,str2)

    print("Concatenated String is: ",result)

if __name__ == "__main__":
    main()