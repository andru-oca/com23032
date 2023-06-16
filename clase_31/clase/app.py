def division(a,b):
    try:
        b = int(b)
        return a/b
    

    except ZeroDivisionError as e:
        print("Zapallo no podés dividir por cero")
        print(e)

    except ValueError as e :
        print(e)

    except Exception as error:
        print(e)



division("1",0)