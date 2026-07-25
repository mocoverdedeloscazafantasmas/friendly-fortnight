class AethraMemory:

    def __init__(self):
        self.storage = {}


    def save(self, key, value):
        self.storage[key] = value


    def recall(self, key):
        return self.storage.get(key)


    def show_memory(self):
        return self.storage



if __name__ == "__main__":

    memory = AethraMemory()

    memory.save(
        "empresa",
        "Empresa de transporte con 15 camiones"
    )

    print(
        memory.recall("empresa")
    )
