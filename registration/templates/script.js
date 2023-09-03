// SIGN-UP
var state = false;
function toggle()
{
    if(state)
    {
        document.getElementById("password").setAttribute("type", "password");
        document.getElementById("eye").style.color='#333333';
        state= false;
    }
    else 
    {
        document.getElementById("password").setAttribute("type", "text");
        document.getElementById("eye").style.color='#73a3f0';
        state = true;
    }
}
function toggle1()
{
    if(state)
    {
        document.getElementById("confirm-password").setAttribute("type", "password");
        document.getElementById("eye-1").style.color='#333333';
        state= false;
    }
    else 
    {
        document.getElementById("confirm-password").setAttribute("type", "text");
        document.getElementById("eye-1").style.color='#73a3f0';
        state = true;
    }
}







