from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Hotline Miami-Inspired Sprite Animations",

    role = "Animator",

    thumbCaption = "Walk cycle",
    
    thumbType = "gif",

    imgRendering = "pixelated",

    galleryImages = [
        GalleryImage("Shoot.gif", "Shooting"),
        GalleryImage("Slide.gif", "Sliding"),
        GalleryImage("DiveRoll.gif", "Dive roll"),
        GalleryImage("Flip.gif", "Flick-flack flip")
    ],


    bodyContent = [
        
        BodyContent("Concepting exercise", r"2024",

            r"""
            At one point, I was considering making a Hotline-Miami-inspired top-down mobile game with unique controls, so I made these animations as a concepting exercise. I found that
            by adding spots on the character with a significantly contrasting values, movement was easier to follow (in this case, meaning his white socks, hands, and shiny bald head :D).
            """

        )
    ]
)
