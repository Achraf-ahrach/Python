# ----------------------------
# ---- Exceptions Handling ---
# ----------------------------


the_file = None
the_treis = 5

while the_treis > 0:

    try: # Try To Open The File

        print("Enter The File Name With Absolute Path To Open")

        print(f"You Have {the_treis} Tries Left")

        print("Example: D:\Python\Exceptions\ExeptionsHandling.py")

        file_name_and_path = input("File Name => : ").strip()

        the_file = open(file_name_and_path, 'r')

        print(the_file.read())

        break
    except FileNotFoundError:
        print("File Not Found Please Be Sure The Name is Valid")

        the_treis -= 1
    except:
        print("Error Happen")

    finally:

        if the_file is not None:
            the_file.close()
            print("File Closed.")

else:

    print("All Tries Is Done")