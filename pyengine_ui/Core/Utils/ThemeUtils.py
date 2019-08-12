def parsetheme(pssstring, folder):
    psslist = pssstring.split("\n")
    i = 0
    while i < len(psslist):
        if psslist[i] != "":
            if psslist[i][0:1] == "//":
                del psslist[i]
        i += 1
    pssstring = "\n".join(psslist)
    pssstring = pssstring.replace("pproperty", "qproperty")
    pssstring = pssstring.replace("plineargradient", "qlineargradient")

    pssstring = pssstring.replace("\\4", "")
    folderlist = folder.split("/")
    if len(folderlist) == 1:
        folderlist = folder.split("\\")
    i=0
    while True:
        if folderlist[i] == "..":
            del folderlist[i]
            del folderlist[i-1]
        i += 1
        if i >= len(folderlist):
            break
    folder = "/".join(folderlist)
    pssstring = pssstring.replace("url(", "url("+folder+"/")

    return pssstring
