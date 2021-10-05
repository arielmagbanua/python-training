class MultiDisplay:
    message = ''
    count = 0

    def set_message(self, message):
        self.message = message
    
    def set_count(self, count):
        self.count = count

    def to_string(self):
        return 'Message: ' + self.message + ', Count: ' + str(self.count)

    def set_display(self, message, count):
        self.message = message
        self.count = count

        self.display()

    def display(self):
        for _ in range(0, self.count):
            print(self.message)

    def get_message(self):
        return self.message

md = MultiDisplay()

md.set_message('Hello World!')
md.set_count(3)
print(md.to_string())
md.display()

md.set_display("Goodbye cruel world!", 2)
print(md.to_string())
print("Current message:", md.get_message())
