def mostComments(submissions):
    # find the post that has the largest amount of comments
    # submissions should be a list
    return sorted(submissions, key = lambda sub: sub['num_of_comments'], reverse=True)

def topTen(submissions):
    # submissions should be a list
    return submissions[0:10]
