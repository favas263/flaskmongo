function checkForm()
{
    pwd = document.getElementById("pwd").value;
    pwd2 = document.getElementById("pwd2").value;

    if(pwd != pwd2)
    {
        document.getElementById("span").innerHTML = "*Passwords not matching";
        return false
    }
    else
    {
        document.getElementById("span").innerHTML = "";
        return true
    }

}