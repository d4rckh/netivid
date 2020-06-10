def handle(scr):
    out = []
    if scr.status == -1:
        out.append("Script did not finished.")
    if scr.status == 0:
        out.append("Script finished successfully.")
    if scr.status == 1:
        out.append("Script failed.")
        if not (scr.error == None):
            out.append(scr.error)
        else:
            out.append("Script did not return an error")
    return out