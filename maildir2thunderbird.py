import sys
import pathlib
import shutil
import imap_tools

# 実行する前にやることを見たいときはTrueにする
DRY_RUN = False

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Usage: {} maildir".format(args[0]))
        exit(1)
    maildir = pathlib.Path(args[1]).absolute()
    name = maildir.name
    subdir = maildir.parent.joinpath("{}.sbd".format(name))

    for subfolder in maildir.glob(".??*"):
        csd = subdir
        for parts in subfolder.name[1:].split("."):
            parts = imap_tools.imap_utf7.decode(parts.encode())
            sd = csd
            csd = sd.joinpath("{}.sbd".format(parts))
            if not sd.exists():
                if DRY_RUN:
                    print("mkdir {}".format(sd))
                else:
                    sd.mkdir()
            newname = parts
        if DRY_RUN:
            print("mv {} {}".format(subfolder, sd.joinpath(newname)))
        else:
            shutil.move(str(subfolder), str(sd.joinpath(newname)))
