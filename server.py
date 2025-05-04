from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(factorial, "calculate_factorial")
print("Server is running on port 8000...")
server.serve_forever()


import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

number = int(input("Enter an integer to compute factorial for: "))
result = server.calculate_factorial(number)
print(f"The factorial of {number} is {result}")

