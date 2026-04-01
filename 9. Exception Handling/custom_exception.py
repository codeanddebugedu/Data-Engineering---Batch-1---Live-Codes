class NotEligibleToVote(Exception):
    pass


try:
    age = 17
    if age < 18:
        raise NotEligibleToVote("Not good age")
except NotEligibleToVote as e:
    print(e)
except:
    print("Some error occurred")
