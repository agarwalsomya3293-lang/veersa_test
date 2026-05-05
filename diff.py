json
{
  "code": "<!DOCTYPE html>
<html>
        <head>
            <meta charset=\"UTF-8\">
            <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
            <title>calculator</title>
            <link rel=\"stylesheet\" href=\"calci.css\">
        </head>
        <body>
            
            <div class=\"frame\">
                <p class=\"heading\">calculator</p>
                <div class=\"display\">
                    <input type=\"text\" id=\"display\" disabled>
                </div>
                <div class=\"button-group\">
                    <input class=\"button\" type=\"button\" value=\"9\" onclick=\"document.getElementById('display').value+='9'\">
                    <input class=\"button\" type=\"button\" value=\"8\" onclick=\"document.getElementById('display').value+='8'\">
                    <input class=\"button\" type=\"button\" value=\"7\" onclick=\"document.getElementById('display').value+='7'\">
                    <input class=\"button\" type=\"button\" value=\"+\" onclick=\"document.getElementById('display').value+='+'\">
                </div>
                <div class=\"button-group\">
                    <input class=\"button\" type=\"button\" value=\"6\" onclick=\"document.getElementById('display').value+='6'\">
                    <input class=\"button\" type=\"button\" value=\"5\" onclick=\"document.getElementById('display').value+='5'\">
                    <input class=\"button\" type=\"button\" value=\"4\" onclick=\"document.getElementById('display').value+='4'\">
                    <input class=\"button\" type=\"button\" value=\"-\" onclick=\"document.getElementById('display').value+='-'\">
                </div>
                <div class=\"button-group\">
                    <input class=\"button\" type=\"button\" value=\"3\" onclick=\"document.getElementById('display').value+='3'\">
                    <input class=\"button\" type=\"button\" value=\"2\" onclick=\"document.getElementById('display').value+='2'\">
                    <input class=\"button\" type=\"button\" value=\"1\" onclick=\"document.getElementById('display').value+='1'\">
                    <input class=\"button\" type=\"button\" value=\"*\" onclick=\"document.getElementById('display').value+='*'\">
                </div>
                <div class=\"button-group\">
                    <input class=\"button\" type=\"button\" value=\"C\" onclick=\"document.getElementById('display').value=''\">
                    <input class=\"button\" type=\"button\" value=\"0\" onclick=\"document.getElementById('display').value+='0'\">
                    <input class=\"button\" type=\"button\" value=\"/\" onclick=\"document.getElementById('display').value+='/'\">
                    <input class=\"button\" type=\"button\" value=\"=\" onclick=\"try{document.getElementById('display').value=eval(document.getElementById('display').value)}catch(e){document.getElementById('display').value='Error'}\">
                </div>
                
            </div>
        </body>
</html>"
}