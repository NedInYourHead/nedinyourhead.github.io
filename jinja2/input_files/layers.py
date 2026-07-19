from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Layers",


    role = "Designer, Artist, Programmer",

    thumbType = "png",

    galleryImages = [
        GalleryImage("screenshot1.png", "Intro screen (leads directly into gameplay)"),
        GalleryImage("screenshot2.png", "Gameplay"),
        GalleryImage("screenshot3.png", "Layers fly offscreen to reveal the next ones underneath.")
    ],


    links = [
        Link("Google Drive download link", "https://drive.google.com/file/d/19Uy0eRhZoJG3qkUeV9SyUiiqgD7iUiJg/view?usp=sharing")
    ],


    bodyContent = [
        
        BodyContent("Portfolio Project", r"January 20, 2026",

            r"""
            <b>Tilt your phone to avoid enemies as you descend... The Layers!</b>
            <br><br>
            The basic premise was for an endless game where you must tilt your phone to avoid enemies and reach the hole leading to the next layer, with more enemies being introduced
            as you progressed through the levels. The question that remained was: what would that progress look like? I cycled through ideas, from an exploration-based metroidbrania, to
            a roguelike, to a boss-rush game, and in the meantime kept myself busy by creating elements I knew would be in all of them, and I feel I got it to look really good. (cont.)
            """

        ),

         BodyContent("Development-oriented feature framing method", r"January 20, 2026",

            r"""
            This process unfortunately forced me to keep my options open, causing the scope to balloon as I tried to accomodate all possible designs and create systems for them. So at a
            certain point, I had to limit my possibilities, and to avoid this situation in the future I devised a method for building components and systems that would reframe it from the
            perspective of people actually working on the project, i.e myself:
            <br><br>
            1. What do developers want to concern themselves with in order to set this component/entity up in-game?
            <br><br>
            2. What do those developers expect the code to do/work out for them automatically?
            <br><br>
            ...And anything between those two questions, I could leave exposed with default values. Using these questions, I built a more limited set of systems and prefabs that could be
            easily expanded on within the reduced scope I picked, limiting scalability, but trusting that I'd be able to refactor and rework those systems when (and if) I got to that point.
            """

        )
    ]
)
