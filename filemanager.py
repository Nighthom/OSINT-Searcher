class FileManager:
    def __init__(self):
        pass
    
    
    def save(self, data):
        filename = input("What file name did you want to save?")
        self.save_file(f"result/{filename}", data)
        
    
    def save_file(self, path ,data):
        print("[~] Saving Files...")
        with open(path, "w") as savedata:
            savedata.write(data)
        print("[~] Save Success!")
