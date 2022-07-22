from apimanager import APICertificator
from searchengine import SearchEngine
from filemanager import FileManager
from logo import LOGO

VERSION = 0.1

def main():
    try:
        print(LOGO)
        print(f"OSINT Searcher v.{VERSION}")
        api = APICertificator()
        engine = SearchEngine(api)
        engine.run()
        
        if input("[*] Did you want to save data?(y/n): ") == "y":
            filemanager = FileManager()
            filemanager.save(engine.result)
        
    except KeyboardInterrupt:
        print("[*] Keyboard Interrupt.")

    print("Bye bye.")

if __name__ == "__main__":
    main()
