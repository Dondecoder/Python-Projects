from pytube import YouTube


class Youtube_link:
    url = input("Please enter the youtube url: ")

    def __init__(self):
        self.yt_url = YouTube(self.url)

    def get_url(self):
        if self.yt_url == self.yt_url:
            print("Thank you for the link")
        else:
            return self.url

class Conversion:

    def __init__(self):
        self.url = Youtube_link.url

    def download (self):
        yt_url = YouTube(self.url)

        if yt_url == yt_url:
            print ("Downloading: ")
            yt_download = yt_url.streams.get_highest_resolution()
            yt_download.download()
        else:
            print("Server error: ")

if __name__ == '__main__':
    yt = Youtube_link()
    yt.__init__()
    yt.get_url()
    yt_download_link = Conversion()
    yt_download_link.download()
