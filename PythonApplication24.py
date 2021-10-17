from collections import deque
class brackets():#Class of name brackets
    #Making a list of brackets.
    Openining_brackets = ["(", "{", "["]
    Closing_brackets = [")", "}", "]"]

    def Check(self, expression): # function to check if the brackets aree equal otr not
        self.stack = deque() #provide memory to stack
        for i in expression: #Loop from 0 to the size of expression
            if i in self.Openinin_gbrackets: #If there's a opening bracket they will be given to the stack
                self.stack.append(i) #appending.
            elif i in self.Closing_brackets: #if there's a closing bracket the bracket will be poped out and it will be matched with the existing bracket
                pos = self.Closing_brackets.index(i)
                if ((len(self.stack) > 0) and (self.Openining_brackets[pos] == self.stack[len(self.stack) - 1])): #if they are same brackets will be poped out.
                    self.stack.pop()
                else:

                    return "Unbalanced"
                if len(self.stack) == 0:
                    return "Balanced"
                else:
                    return "Unbalanced"


object = brackets() # object of class
expression=input("Input any expression: ")
print(object.Check(expression))#Calling of function to check expression
