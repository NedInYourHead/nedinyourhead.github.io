from project_site_data import Link, ProjectSiteData


project_data = ProjectSiteData(

    #Title
    "Flappy Bird With A Laser",

    #Role
    "Sole Developer",

    #Header Code
    "",

    #Thumbnail File Type 
    "png",

    #Other Gallery Images
    ["screenshot2.png", "screenshot1.png", "OGscreenshot1.png"],

    #Links
    [
        Link("Web Version (OG) + Itch.io Download Page", "https://nedinyourhead.itch.io/flappy-bird-with-a-laser"),
        Link("Mobile Version (Google Drive)", "https://drive.google.com/file/d/1Zoho5zXNKHKdxxLKZZdnntTU2RF0wCNY/view?usp=drive_link")
    ],

    #Intro Paragraph
    "Flappy bird with a twist! Use a second button to zap enemies out of the air, while avoiding the robo-pipes coming your way.",

    #Description
    r"""
    Flappy bird with a laser was originally conceived as a response to our "Modding Brief" at Falmouth University, but upon playing their Flappy Bird starter project (<i>adding</i> momentum when you jump, really?), I figured that the only thing to do was to recreate Flappy Bird in Unity from scratch :).
    <br><br>
    For our portfolio project, my aim was to build two out of three mobile apps and make a website over the course of seven weeks. For my third project, I decided I would save the concepting and port one of my older projects to mobile, and this was the natural choice. 
    <br><br>
    This did bring some design problems though - wanting to recreate the portrait mode from the original, the missile enemies from the original were impossible to predict, and the art style was far too noisy for such a small resolution. So in order to keep the enemies on the screen a bit longer, I decided to utilise DOTween to have them enter the screen, hang around a bit, before attaching to the background and accelerating forward, creating thematic "Hawk" sprites to match.    </p>
    </div>
    """
)
