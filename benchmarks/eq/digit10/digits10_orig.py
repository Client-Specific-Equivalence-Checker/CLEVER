def lib(n):
    result =1
    counter = 10
    while (n > counter):
        result +=1
        counter = counter * 10
        if (n > counter):
            result +=1
            counter = counter * 10
            if (n > counter):
                result +=1
                counter = counter * 10
                if (n > counter):
                    result +=1
                    counter = counter * 10

    
    return result


def digits10(x):
    return lib(x)