from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Bar For Bar",


    role = "Programmer, Artist, Designer",


    thumbType = "png",


    galleryImages = [
        GalleryImage("screenshot1.jpeg", "Gameplay"),
        GalleryImage("screenshot2.jpeg", "\"arcade demo\" main menu"),
        GalleryImage("screenshot3.jpeg", "Both players ready"),
        GalleryImage("screenshot4.jpeg", "Rematch?"),
        GalleryImage("bar for bar diagram.png", "Gameplay flowchart")
    ],


    links = [
        Link("Itch.io page", "https://nedinyourhead.itch.io/bar-for-bar"),
        Link("Google Drive download link", "https://drive.google.com/file/d/12FaS-cmfCMEWphYliwLMAAC4jCiWyqy6/view?usp=drive_link")
    ],


    bodyContent = [
        
        BodyContent("Portfolio Project", r"January 20, 2026",

            r"""
            <b>Fill your bar before your opponent, but be careful not to leave yourself open to attack!</b>
            <br><br>
            Bar for Bar is one of three mobile games I developed for my portfolio project at Falmouth. The main design aim here was to keep it simple, focusing on building tools to make my job easier in the next projects - So I decided to make a game that took full advantage of the new UI components I was building.
            <br><br>
            I started with the humble progress bar. A UI element that can either be full, empty, or somewhere in-between; the simplest representation of a number between two extents; and yet it's been used to represent life experience, physical wellbeing, progress towards a goal and much, much more. 
            <br><br>
            Moreover, I figured that an empty bar presents a clear goal to the player: Fill it up! Therefore, two players are tasked with the goal of filling their bar up first, and utilised my newly-coded multi-touch input to bind tapping, holding and releasing to different actions. Finally I came up with a set of actions that would balance each other out, drawing from the "Slap Game" of my schoolhood days:
            <br><br>Tap - Attack (damage the other player and gain progress if they aren't Blocking)
            <br><br>Hold - Fill (fill up your progress bar)
            <br><br>Release - Block (slowly lose progress, but gain progress if Attacked)
            """
        )
    ]
)
