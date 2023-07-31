def add(x,y):
    return x+y
def substarct(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def calcukator():
    x=int(input("enter premier number : "))
    y=int(input("enter deuxieme  number : "))
    op=["+","-","*","/"]
    print("the available operations are  : ")
    for i in op :
        print(i," ")
    while True :
        s=input("select an operation : ")
        if s in op :
            if s=="+":
                print(x,"+",y,"=",add(x,y))
                print(" du you want to use the result as the premier num ? ")
                ans=input("(y/n): ")
                if ans=="y" :
                    x=add(x,y)
            elif s=="-":
                print(x,"-",y,"=",substarct(x,y))
                print(" du you want to use the result as the premier num ? ")
                ans=input("(y/n): ")
                if ans=="y" :
                    x=substarct(x,y)
            elif s=="*" :
                print(x,"×",y,"=",multiply(x,y))
                print(" du you want to use the result as the premier num ? ")
                ans=input("(y/n): ")
                if ans=="y" :
                    x=multiply(x,y)
            elif s=="/" :
                print(x,"/",y,"=",divide(x,y))
                print(" du you want to use the result as the premier num ? ")
                ans=input("(y/n): ")
                if ans=="y" :
                    x=divide(x,y)

        else:
            break
calcukator()
        
