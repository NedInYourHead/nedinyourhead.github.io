from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Energy",

    role = "Cover Designer, Selector",

    thumbCaption = "<i>Energy</i> original cover",

    thumbType = "png",

    imgRendering = "auto",

    galleryImages = [
        GalleryImage("mix-cover1.png", "<i>Audacity mix</i> cover")
    ],


    links = [
        Link("Energy playlist on spotify", "https://open.spotify.com/playlist/5iM301XZigzV0nw1YCMpXx"),
        Link("Energy playlist (Audacity mix) on spotify", "https://open.spotify.com/playlist/77eEb6qU62QtdSglfNKZrj")
    ],


    bodyContent = [

        BodyContent("Audacity Mix", r"2025",

            r"""
            <b>The immovable object to the unstoppable force of my Energy playlist.</b>
            <br><br>
             My Audacity Mix was selected for non-movement heavy games, that still otherwise benefitted from an energetic soundtrack. Whereas I'd describe the rhythms of Energy as a
             whole as "leaning forwards", and Chill as "leaning backward", this mix is perfectly upright, stamping the ground as shown in this cover variant...
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/77eEb6qU62QtdSglfNKZrj?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        ),
        
        BodyContent("Energy Playlist", r"2021",

            r"""
            <b>Explosive, rapid tracks that'll get you pumped. Run and jump!</b>
            <br><br>
            I made this playlist originally as a gaming playlist, but it more generally embodies the feeling of kinetic energy and jumping obstacles - hence the silhouettes of hands
            visible in the explosion.
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5iM301XZigzV0nw1YCMpXx?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        )
    ]
)
