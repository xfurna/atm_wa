from _install_ import INSTALL
import wd
import argparse
import targets
import sys


a = argparse.ArgumentParser()
if len(sys.argv[1:]) == 4:
    a.add_argument("--PATH", "-p", help = "Complete path of latest release of gekodriver in quotes")
a.add_argument("--COUNT", "-c", help = "Number of targets that you want to feed in")
a.add_argument("--MSG", "-m", help = "Your message in quotes")
a.add_argument("--get", "-i", help = "Give it 'y' if you want automatic installation [RISK]")

args = a.parse_args()

if args.get == 'y':

    if len(sys.argv[1:]) == 3:
        targets.PATH = "~/Downloads/gekodriver/"
    else:
        targets.PATH = args.PATH
    targets.cmnds.append("PATH=$PATH:" + targets.PATH + "; export PATH")
    install = INSTALL()
    install.Install()

    input("CONTINUE-")



targets.msg += args.MSG
for i in range(int(args.COUNT)):
    targets.recipient.append(input("Enter the recipient's ID  (one by one)  "))

wd.drive()
