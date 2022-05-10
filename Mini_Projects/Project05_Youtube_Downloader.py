from pytube import YouTube

#link = input("Please input your link: ")
link = "https://www.youtube.com/watch?v=sngQiOXMaWs"

yt = YouTube(link)

print(yt.title)
print("Number of views: ", yt.views)
print("Length of Video: ", yt.length,"seconds")
#print("Quality, ", yt.streams)
#print("Description: ", yt.description)
print("Ratings: ", yt.rating)
print(yt.streams)

