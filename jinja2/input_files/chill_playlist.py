from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Chill",

    role = "Cover Designer, Selector",

    thumbCaption = "<i>Chill</i> original cover",

    thumbType = "png",

    imgRendering = "auto",

    galleryImages = [
        GalleryImage("mix-cover1.png", "<i>Evening mix</i> cover"),
        GalleryImage("mix-cover2.png", "<i>Breakfast mix</i> cover")
    ],


    links = [
        Link("Chill playlist on spotify", "https://open.spotify.com/playlist/5iM301XZigzV0nw1YCMpXx"),
        Link("Chill playlist (Evening mix) on spotify", "https://open.spotify.com/playlist/77eEb6qU62QtdSglfNKZrj"),
        Link("Chill playlist (Breakfast mix) on spotify", "https://open.spotify.com/playlist/3ffiWUa70Uq71mvB8jX5D1")
    ],


    bodyContent = [

        BodyContent("Breakfast Mix", r"2026",

            r"""
            <b>Selections from my Chill playlist so you can start the day damn right.</b>
            <br><br>
            This cover shows the egg from the previous covers being fried on a gas stove for breakfast, with some piping-hot coffee. The horizontal pavement is replaced with vertical
            wall tiling, and the double yellow-lines become stovetop grills. This mix features the more jazzy and bluesy songs on the playlist, a perfect backdrop for the morning ritual.
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3ffiWUa70Uq71mvB8jX5D1?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        ),

        BodyContent("Evening Mix", r"2025",

            r"""
            <b>Low-key, classy tunes from my Chill playlist, to play as the evening gets chillier...</b>
            <br><br>
            Some songs from my Chill playlist are a much easier listen as it falls to dusk - My Evening selection consists of only the most suave, contemplative songs from the playlist.
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/31bqhVpfRyDvFLMy3RjAA8?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        ),
        
        BodyContent("Chill Playlist", r"2021",

            r"""
            <b>Beats to beat the summer heat.</b>
            <br><br>
            This is my go-to coding playlist and a must-have for the summer. I find it helps to recontextualise the heat as "relaxing" rather than "inescapable", and always reminds me of
            summers spent chilling in London Fields with my mates.
            <br><br>
            I designed the cover in reference to the Hackney streets I spent afternoons on, as well as the aphorism "It's hot enough to fry an egg on the sidewalk!"
            <br><br>
            <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/4oq6W8CysrXpWo59tHrkAS?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """
        )
    ]
)
