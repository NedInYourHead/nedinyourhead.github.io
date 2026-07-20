from project_site_data import ProjectSiteData, Link, GalleryImage, BodyContent


project_data = ProjectSiteData(
    
    title = "Just The Link Select Cursors",


    role = "Art, Animations, Formatting",


    headerCode = r"""<style type="text/css">
                      body {cursor: url("https://www.rw-designer.com/cursor-set/oops-all-link-selects"), auto;}
                      </style>
                      """,


    thumbType = "png",

    imgRendering = "pixelated",

    galleryImages = [
    ],


    links = [
        Link("Just The Link Select Cursors at RW Cursor Gallery", "https://www.rw-designer.com/cursor-set/oops-all-link-selects")
    ],


    bodyContent = [
        
        BodyContent("Linky the Link Select Hand", r"August 28, 2023",

            r"""
            <b>Did you ever think, "Gee, I wish the rest of my cursor roles were as quirky and awesome as the link select hand"? Well I did, and now you have this cursor pack!</b> Fully
            animated and tweaked to work against any background.
            <br><br>
            Some of the cursors make use of inverted colours for detailing: precision select holds an inverted cross, help is surrounded by a bunch of question marks, and the location/
            person select cursors have their icons in inverse.
            <br><br>
            I created all cursors (apart from the classic link select cursor, which is credited to Windows) and their animations in Aseprite, before porting it over to RW Cursor editor
            for testing/formatting. I tested this pack to make sure it felt extra smooth and fun to use. Let me know what you think!
            """

        )
    ]
)
