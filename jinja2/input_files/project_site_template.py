from project_site_data import Link, ProjectSiteData


project_data = ProjectSiteData(

    #Title
    "Project Template",

    
    #Header Code
    r"",

    #Role
    "Role On The Project",

    #Thumbnail File Type
    "png",

    #Other Gallery Images
    ["screenshot1.png", "screenshot2.png"],

    #Links
    [
        Link("Link1", "https://link1.com"),
        Link("Link2", "https://link2.com")
    ],

    #Intro Paragraph
    "Intro paragraph, summarise the project",

    #Description
    r"""
    html-formatted description. Use
    <br><br>
    to separate paragraphs, and feel free to add code, links, or whatever you like.
    """
)
