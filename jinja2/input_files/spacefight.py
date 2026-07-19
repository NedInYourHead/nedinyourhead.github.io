from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Spacefight",


    role = "Programmer, Designer, Artist",
    

    thumbType = "png",

    imgRendering = "pixelated",

    galleryImages = [
        GalleryImage("screenshot1.png", "Main menu"),
        GalleryImage("screenshot2.png", "Gameplay"),
        GalleryImage("screenshot3.png", "How to play")
    ],


    links = [
        Link("Itch.io page + web version", "https://nedinyourhead.itch.io/spacefight")
    ],


    bodyContent = [
        
        BodyContent("Uni Project", r"November 27, 2025",

            r"""
            Spacefight was made as a uni project, to prototype some of the basic elements of a concept I had for a more fleshed-out zero-g fighting game, as well as to figure out how
            Unity's physics system actually works. Because this was a solo project, I decided to make all assets myself (including the fonts! Though excluding the suave music that plays
            when you spend too long in the main menu :P).
            <br><br>
            Taking inspiration from the 2016 mobile game <i>Ultra Fighting Bros</i>, players are placed in a box, floating through space, which is occasionally sent careening by stray
            meteors, sending it spinning. This creates a unique challenge where players try to touch each other on the wall while their opponent is on moving ground. To make this more
            interesting, players must try and orient themselves in the air to land upright on the wall if they want to minimise their stun period.
            <br><br>
            Other modifiers that the ship would float through in the full concept include gravity zones, turbulence, and more, with full fighting-game movesets for the players, and
            floating crates with items and weapons.
            """

        )
    ]
)
