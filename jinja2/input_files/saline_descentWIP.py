from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Saline Descent",

    role = "Programmer",

    headerCode = r"",

    thumbCaption = r"'Charley' Monster",

    thumbType = "png",

    imgRendering = "auto",

    galleryImages = [
        GalleryImage("screenshot1.png", "First screenshot"),
        GalleryImage("screenshot2.png", "Second screenshot")
    ],


    links = [
        Link("Download on Itch.io", "https://joshua-apotheosis.itch.io/saline-descent")
    ],


    bodyContent = [
        
        BodyContent("UnityEvents Trigger Components", r"July 28, 2026",

            r"""
            <b>Placeholder Text</b>
            <br><br>
            As a systems programmer for Saline Descent, our first-person horror project at Falmouth, I was tasked with creating a set of components to facilitate level design. Due to
            their ease-of-use out-of-the-box in the inspector, I chose to utilise Unity’s Events System, and created a set of triggerable components, such as a timer which invokes
            after a time limit, a one-time trigger box, and a toggle which alternates between two sets of events or can be set directly. Because of their reliance on Events, designers
            could chain these components, lego-style in-editor, to create in-game logic, puzzles and action sequences in a logical, hands-on way.
            """

        )
    ]
)
