from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Nights",

    role = "Cover Designer, Selector",

    thumbCaption = "<i>Nights</i> original cover",

    thumbType = "png",

    imgRendering = "auto",

    galleryImages = [
        GalleryImage("mix-cover1.png", "<i>Pop mix</i> cover")
    ],


    links = [
        Link("Nights playlist on spotify", "https://open.spotify.com/playlist/172ztGQay5po10tABASVuM"),
        Link("Nights playlist (Pop mix) on spotify", "https://open.spotify.com/playlist/6ggkET4YsF2QmCySWR0eic")
    ],


    bodyContent = [

        BodyContent("Pop Mix", r"May, 2024",

            r"""
            <b>A more palatable introduction to my night-time playlist. Lyric songs favoured.</b>
            <br><br>
             My <i>Nights</i> playlist can get a bit experimental and ambient, so this Pop Mix contains the most easy-listening songs of the lot. It was originally created for my friends when they were
             staying over in London, and a couple of them couldn't get into the music without lyrics!
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/6ggkET4YsF2QmCySWR0eic?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        ),
        
        BodyContent("Nights Playlist", r"2019",

            r"""
            <b>Songs found behind a lamppost, in the canal, under a council housing estate, within a cul-de-sac, around a bridge painted with graffiti.</b>
            <br><br>
            Before I got spotify, before I got an MP3 player, I used to go home on the bus after dark during the winter, and I always enjoyed watching the lights of the city out the
            window as it went by, humming this music in my head. 
            <br><br>
            So as soon as I could get my hands on an MP3 player, I immediately started loading songs onto it to capture that feeling, and these would be the tracks I'd listen to as I
            wandered London on my scooter during my teenage years. 8 years on from that and counting, I've kept adding to this playlist to this day.
            <br><br>
            Listen and Enjoy!
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/172ztGQay5po10tABASVuM?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        )
    ]
)
