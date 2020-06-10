from utils.arguments import args
from utils.scriptfinishhandler import handle
from utils.logging.banner import printBanner
from utils.logging.logresults import logResults
import importlib.util

printBanner()

def callScript(script):
    spec = importlib.util.spec_from_file_location("scripts.script", "source/script/" + script + ".py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    MainClass = foo.MainClass(args.target)
    if args.type in MainClass.accept:
        MainClass.main()
        logResults(MainClass, args.target, handle(MainClass))

if not (args.script == None) and not (args.target == None) and not (args.type == None):    
    for script in args.script.split(","):
        callScript(script)