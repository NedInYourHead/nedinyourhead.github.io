from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Flappy Bird With A Laser",


    role = "Programmer, Artist, Animator",


    headerCode = r"",


    thumbType = "png",


    galleryImages = [
        GalleryImage("screenshot1.jpeg", "Mobile port main menu"),
        GalleryImage("screenshot2.jpeg", "Mobile port gameplay"),
        GalleryImage("OGscreenshot1.png", "OG web version")
    ],


    links = [
        Link("Itch.io page + web version", "https://nedinyourhead.itch.io/flappy-bird-with-a-laser"),
        Link("Google Drive apk download", "https://drive.google.com/file/d/1Zoho5zXNKHKdxxLKZZdnntTU2RF0wCNY/view?usp=drive_link")
    ],


    bodyContent = [
        
        BodyContent("Mobile Port", "July 08, 2026",

            r"""
            <b>Flappy bird with a twist! Use a second button to zap enemies out of the air, while avoiding the robo-pipes coming your way.</b>
            <br><br>
             For our portfolio project, my aim was to build two out of three mobile apps and make a website over the course of seven weeks. For my third project, I decided I would save the
             concepting and port one of my older projects to mobile, and this was the natural choice. 
            <br><br>
            This did bring some design problems though - wanting to recreate the portrait mode from the original, the missile enemies from the original were impossible to predict, and
            the art style was far too noisy for such a small resolution. So in order to keep the enemies on the screen a bit longer, I decided to utilise DOTween to have them enter the
            screen, hang around a bit, before attaching to the background and accelerating forward, creating thematic "Hawk" sprites to match.
            """
        ),

        BodyContent("Original Web Version", "November 14, 2023",

            r"""
            <b>Flappy bird with a twist! Use a second button to zap enemies out of the air, while avoiding the robo-pipes coming your way.</b>
            <br><br>
             For our portfolio project, my aim was to build two out of three mobile apps and make a website over the course of seven weeks. For my third project, I decided I would save the
             concepting and port one of my older projects to mobile, and this was the natural choice. 
            <br><br>
            This did bring some design problems though - wanting to recreate the portrait mode from the original, the missile enemies from the original were impossible to predict, and
            the art style was far too noisy for such a small resolution. So in order to keep the enemies on the screen a bit longer, I decided to utilise DOTween to have them enter the
            screen, hang around a bit, before attaching to the background and accelerating forward, creating thematic "Hawk" sprites to match.
            """
        )
    ]
)
