class Memory:
    def __init__(self):
        self.data = {}

    def remember(self, key, value):
        self.data[key] = value

    def recall(self, key):
        return self.data.get(key, "No memory found.")

    def forget(self, key):
        return self.data.pop(key, None) is not None

    def show(self):
        if not self.data:
            print("Memory bank empty.")
            return
        for key, value in self.data.items():
            print(f"• {key}: {value}")
