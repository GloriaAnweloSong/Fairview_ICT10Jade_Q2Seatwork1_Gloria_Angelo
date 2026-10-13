from pyscript import document, display

def checkName(e):

    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value

    name = (fname + lname).lower

    mem_list = ["john legend", "john pork", "john lennon", "john cage", "john roblox"]
    
    confirm_name = name in mem_list

    message = (f'Sorry {(name).capitalize}, your name is not found.' , f'Yay! {(name).capitalize}, your name is found.')

    document.getElementById('result').innerHTML = message[confirm_name]