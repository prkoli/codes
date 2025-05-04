from xmlrpc.server import SimpleXMLRPCServer

def calculate(a, b, operation):
    try:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                return "Error: Division by zero"
            return a / b
        else:
            return "Error: Unsupported operation"
    except Exception as e:
        return f"Server error: {str(e)}"

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(calculate, "remote_calculate")
print("Server is running on port 8000...")
server.serve_forever()

import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    result = server.remote_calculate(a, b, operation)
    print(f"Result: {result}")

except Exception as e:
    print("Client error:", e)
