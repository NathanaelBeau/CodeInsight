var0 = "login.php"
var1 = "newlogin.php"
var2 ="""<html>
    <head>
        <title>Forms</title>
    </head>
    <body>
    <form action="login.php" method="post">
        Username: <input type="text" name="username" value="" />
        <br />
        Password: <input type="password" name="password" value="" /> 
        <br />
        <input type="submit" name="submit" value="Submit">
    </form>
    </body>
</html>"""
expected_result =  '<html>\n    <head>\n        <title>Forms</title>\n    </head>\n    <body>\n    <form action="newlogin.php" method="post">\n        Username: <input type="text" name="username" value="" />\n        <br />\n        Password: <input type="password" name="password" value="" /> \n        <br />\n        <input type="submit" name="submit" value="Submit">\n    </form>\n    </body>\n</html>'
result = test(var0, var1, var2)
assert expected_result == result, 'Test failed'