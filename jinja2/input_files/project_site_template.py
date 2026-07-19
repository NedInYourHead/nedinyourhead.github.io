from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Project Title",


    role = "Role On The Project",


    headerCode = r"",


    thumbType = "png",

    imgRendering = "auto",

    galleryImages = [
        GalleryImage("screenshot1.png", "First screenshot"),
        GalleryImage("screenshot2.png", "Second screenshot")
    ],


    links = [
        Link("Link1", "https://link1.com"),
        Link("Link2", "https://link2.com")
    ],


    bodyContent = [
        
        BodyContent("Update Title", r"Month DD, YYYY",

            r"""
            <b>Placeholder Text</b>
            <br><br>
            This is some placeholder text to be featured in the body of the
            project website.
            """

        )
    ]
)
