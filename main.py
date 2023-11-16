import pytube

url = input("enter video URL :  ")

path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)