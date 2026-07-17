from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
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

        )
    ]
)
