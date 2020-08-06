def sqrRoot(num):
    guess = num/2
    for i in range(30):
        guess = (1/2)*(guess+(num/guess))
    return "%.2f" % guess


print(sqrRoot(347832))
