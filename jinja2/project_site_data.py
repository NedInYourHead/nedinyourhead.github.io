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
                 thumbCaption: str = "",
                 thumbType: str = "png",
                 imgRendering: str = "auto",
                 galleryImages: list[GalleryImage] = list[GalleryImage],
                 links: list[Link] = list[Link],
                 bodyContent: list[BodyContent] = list[BodyContent]
                 ):

        self.data = {
            "title": title,
            "role": role,
            "headerCode": headerCode,
            "thumbCaption": thumbCaption,
            "thumbType": thumbType,
            "imgRendering": imgRendering,
            "galleryImages": galleryImages,
            "links": links,
            "bodyContent": bodyContent
        }

    def __str__(self):
        return self.data["title"]

    __repr__ = __str__
    


testEmptyProject = ProjectSiteData()
