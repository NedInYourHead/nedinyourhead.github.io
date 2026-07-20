from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Chaos Balls",


    role = "Designer, Programmer, Artist",

    thumbType = "png",

    imgRendering = "pixelated",

    galleryImages = [
        GalleryImage("screenshot1.png", "Gameplay")
    ],


    links = [
        Link("Chaos Balls on Itch.io", "https://nedinyourhead.itch.io/chaos-balls")
    ],


    bodyContent = [
        
        BodyContent(r"<i>It's a Winter Wonder-Jam!</i>", r"January 02, 2023",

            r"""
            <b>Organise as many balls as possible in 60 seconds by whacking them into the goals using your baseball bat- but be careful, as getting hit by one will lead to an instant
            game-over!</b>
            <br><br>
            A game made in 6 days for GavinCraft's It's a Winter Wonder-Jam! with the prompt: "Organised-Chaos", as part of a series of jams in which I attempted to learn Godot. This
            was the last of three, and although she's not a looker, the outcome was more than fun enough for me to consider the attempt a success.
            <br><br>
            I hope you'll have as much fun as I did with it!
            """

        )
    ]
)
