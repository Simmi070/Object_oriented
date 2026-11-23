class Account:
    def __init__(self,owner,pin="1234"):
        self.owner = owner
        self.__pin = pin

    def _is_valid_pin(self, new_pin):
        return isinstance(new_pin, str) and len(new_pin) == 4 and new_pin.isdigit()
    def show_pin_status(self):
        print(f"PIN is set({len(self.__pin)}digits)and protected")

    def check_pin(self,entered_pin):
        if entered_pin == self.__pin:
            print("PIN verified! Access granted")
            return True
        else:
            print("Invalid PIN. Access denied")
            return False
    def __str__(self):
        return f"Account Holder: {self.owner} \ PIN Status: Protected"

acc = Account("Simran", "1234")
print(acc)
acc.show_pin_status()
acc.check_pin("1234")     
acc.__pin = "9999"       
acc.check_pin("9999")     
