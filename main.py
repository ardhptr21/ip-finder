import func
import utils


if __name__ == "__main__":
    while True:
        print("=====Ip Finder=====")
        print("[1] Find My IP")
        print("[2] Find Public IP")
        print("[0] Exit")

        choice = input(">> ")

        if choice == "1":
            utils.clearConsole()
            func.getMyIp()
        elif choice == "2":
            utils.clearConsole()
            func.getTheIp()
        elif choice == "0":
            break
        else:
            utils.clearConsole()
            print("Invalid Input")

        input("\nPress Enter to continue...")
        utils.clearConsole()
