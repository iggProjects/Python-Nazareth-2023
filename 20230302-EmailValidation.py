"""  
THIS SCRIPT IS FOR CHECK EMAIL SYNTAXIS

"""
# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors as Col

# CONSTANT SECTION
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"

# FUNCIONS SECTION



#
# ---------- MAIN ----------
#
if __name__ == "__main__":

    print(Col.frGREEN("\n---------- main ----------\n"))
    MyFunc.pause()

    # code
    from email_validator import validate_email, EmailNotValidError

    email = "jo.gainzrain@aulanznet"
    is_new_account = True # False for login pages

    try:
        # Check that the email address is valid.
        validation = validate_email(email, check_deliverability=is_new_account)

        # Take the normalized form of the email address
        # for all logic beyond this point (especially
        # before going to a database query where equality
        # may not take into account Unicode normalization).  
        email = validation.email
        print(f"{email} is OK\n")
    except EmailNotValidError as e:
        # Email is not valid.
        # The exception message is human-readable.
        print(Col.frRED(f"Opssss, your email doesn't have correct syntaxis\n"))
        #print((Col.frGREEN(f"\n---------- INFO FOR OBJECT '{obj}' ----------\n")))
        print(str(e))



    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    moreData=False
    moreData=MyFunc.Y_N("Do you want to see vars characteristics? (Y,N): ")
    
    if moreData:    
        obj='HOLA'    # for example
        print(Col.frGREEN(f"\n---------- INFO FOR OBJECT '{obj}' ----------\n"))
        MyFunc.pause()
        MyFunc.mostrar(obj)
        MyFunc.desc_obj_method(obj)  
    else:
        print((Col.frGREEN("\n---------- That's all for today 👌 ----------\n")))

else:
    # something wrong
    print(Col.frRED("\n---- upsssssssss something is wrong 😢😢  ---\n"))
    MyFunc.pause()

    