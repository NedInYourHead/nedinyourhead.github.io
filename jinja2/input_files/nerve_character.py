from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Nerve Character",

    role = "Animator",

    thumbCaption = "Walk cycle",
    
    thumbType = "gif",

    imgRendering = "auto",

    galleryImages = [
        GalleryImage("NerveRun.gif", "Run cycle"),
        GalleryImage("NerveJump.gif", "Jump"),
        GalleryImage("NerveSit.gif", "Sitting down")
    ],


    bodyContent = [
        
        BodyContent("Nervy and the Quest for Serotonin", r"2025",

            r"""
            <b>I created this character on a whim, when I was experimenting with creating a walk cycle that felt 3D by using points then connecting them for limbs. I found the lanky
            little thing adorable, and came up with a game concept around it - <i>Nervy, and the Quest for Serotonin!</i></b>
            <br><br>
            It would be an auto-platformer, where you're observing this little nerve through a microscope or a tank window, and can drag eyedroppers or pipes around that create puddles
            of various biological hormones, each triggering a different behaviour in Nervy. Adrenaline would make it run faster, and Cortisol would make it jump in fright, for example.
            The aim would be to get to a serotonin puddle at the end of the level while avoiding any hazards along the way, where you can see Nervy sit down and finally relax.
            """

        )
    ]
)
