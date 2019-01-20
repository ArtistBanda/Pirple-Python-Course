# Python homework 2
# Fucntion

def Artist():
    return "Post Malone and Swae Lee"

def Genre():
    return "Pop"

def Title():
    return "Sunflower"

def DurationInSeconds():
    return 159

def check(Artist):
    if Artist == 'Post Malone and Swae Lee':
        return True
    else:
        return False

Artist = Artist()
Genre = Genre()
Title = Title()
DurationInSeconds = DurationInSeconds()
print(Artist, Genre, Title, DurationInSeconds, check(Artist))