import re


def frontpages():
    for pagename in ['index', 'blog', 'research']:
        page = []
        page += build_top(pagename)
        page += build_frontcontent(pagename)
        page += build_bottom(pagename)
        with open("../{0}.html".format(pagename), "w") as outfile:
            outfile.write("".join(page))


def build_top(pagename):
    page = []
    titleDict = {"index" : "About", "blog" : "Blog", "research" : "Research"}
    with open("../skel/top.html", 'r') as topmatter:
        for line in topmatter:
            # Set title of page
            if re.search("<title>", line):
                page.append("    <title>{0} | Jack Baker</title>\n".format(titleDict[pagename]))
            # Highlight correct page button
            elif re.search("class=\"menu\" href=\"{0}.html\"".format(pagename), line):
                page.append(get_shaded_button(pagename, titleDict))
            else:
                page.append(line)
    return(page)


def build_frontcontent(pagename):
    page = []
    with open("../frontpages/{0}.html".format(pagename)) as content:
        for line in content:
            page.append(" " * 3 * 4 + line)
    return page

def build_bottom(pagename):
    page = []
    with open("../skel/bottom.html") as bottommatter:
        for line in bottommatter:
            page.append(line)
    return(page)


def get_shaded_button(pagename, titleDict):
    button_txt = titleDict[pagename]
    button = " " * 3 * 4 + "<li class=\"active\">"
    button += "<a class=\"menu\" href=\"{0}.html\">{1}</a></li>\n".format(pagename, button_txt)
    return(button)


if __name__ == '__main__':
    frontpages()
