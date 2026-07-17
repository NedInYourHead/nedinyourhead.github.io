

class Link(dict):

    def __init__(self, name: str, address: str):
        self.update({"name": name,
                     "address": address})


    def __str__(self):
        return self["name"] + "(" + self["address"] + ")"
    
    __repr__ = __str__



class GalleryImage(dict):

    def __init__(self, filename: str, caption: str):
        self.update({"filename": filename,
                     "caption": caption})


    def __str__(self):
        return self["filename"] + "(" + self["caption"] + ")"
    
    __repr__ = __str__



class BodyContent(dict):

    def __init__(self, title: str, date: str, content: str):
        self.update({
            "title": title,
            "date": date,
            "content": content})


    def __str__(self):
        return self["contentTitle"] + "(" + self["date"] + ")"
    
    __repr__ = __str__




class ProjectSiteData(dict):
    def __init__(self, title: str = "Placeholder Title",
                 role: str = "Placeholder",
                 headerCode: str = "",
                 thumbType: str = "png",
                 galleryImages: list[GalleryImage] = list[GalleryImage],
                 links: list[Link] = list[Link],
                 bodyContent: list[BodyContent] = list[BodyContent]
                 ):

        self = {
            "title": title,
            "role": role,
            "headerCode": headerCode,
            "thumbType": thumbType,
            "galleryImages": galleryImages,
            "links": links,
            "bodyContent": bodyContent
        }

    def __str__(self):
        return self["title"]

    __repr__ = __str__
    


testEmptyProject = ProjectSiteData()

testproject = ProjectSiteData(
    
    title = "Project Title",


    role = "Role On The Project",


    headerCode = r"",


    thumbType = "png",


    galleryImages = [
        GalleryImage("screenshot1.png", "First screenshot"),
        GalleryImage("screenshot2.png", "Second screenshot")
    ],


    links = [
        Link("Link1", "https://link1.com"),
        Link("Link2", "https://link2.com")
    ],


    bodyContent = [
        
        BodyContent("Without embed:", r"Month DD, YYYY",

            r"""
            Before I got spotify, before I got an MP3 player, I used to go home on the bus after dark during the winter, and I always enjoyed watching the lights of the city out the window as it went by, humming this music in my head. 
            <br><br>
            So as soon as I could get my hands on an MP3 player, I immediately started loading songs onto it to capture that feeling, and these would be the tracks I'd listen to as I wandered London on my scooter during my teenage years. 8 years on from that and counting, I've kept adding to that playlist to this day.
            """

        ),

        
        BodyContent("With embed:", "Month DD, YYYY",

            r"""
            Before I got spotify, before I got an MP3 player, I used to go home on the bus after dark during the winter, and I always enjoyed watching the lights of the city out the window as it went by, humming this music in my head. 
            <br><br>
            So as soon as I could get my hands on an MP3 player, I immediately started loading songs onto it to capture that feeling, and these would be the tracks I'd listen to as I wandered London on my scooter during my teenage years. 8 years on from that and counting, I've kept adding to that playlist to this day.
            <br><br>
            This one can get a bit experimental and ambient, so my Pop Mix contains the most easy-listening songs of the lot. It was originally created for my friends when they were staying over in London, and a couple of them couldn't get into the music without lyrics!
             <br><br>
            Listen and enjoy!
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/172ztGQay5po10tABASVuM?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/6ggkET4YsF2QmCySWR0eic?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        )
    ]
)
