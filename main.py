def CheckFizzBuzz(request):
    data = request.args.to_dict()
    try:
        x = int(data.get('n'))
        if x%15==0:
            return "FizzBuzz"
        elif x%3==0:
            return "Fizz"
        elif x%5==0:
            return "Buzz"
        else:
            return str(x)
    except:
        return "ERROR:n is not number"