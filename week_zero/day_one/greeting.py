def greet(input):
    if "hello" in input:
#        print("hello, there")
        return "hello, there"
    else:
#        print("I'm not sure what you mean")
      return "I'm not sure what you mean"


greeting = greet("hello, computer?")
#print(greeting)
#print("Hm, " + greeting)
print(greeting + " David")
