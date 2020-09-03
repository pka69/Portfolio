from flask import Flask, request

def build_page(title, content):
    base = '''<html>
    <head>
        <title>{}</title>
    </head>
    <body>
        <h3>{}</h3>
        <hr/>
            {}
        <hr/>
        &copy;2020
    </body>
    </html>
    '''
    return base.format(title,title,content)

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def guess_my_number():
    def factorial ( s= 1):
        result = 1
        for i in range(1,s +1):
            result*= i
        return result

    if request.method == 'POST':
        n = int(request.form["n"])
        n1 = 2**n
        n2 = n**n
        n3 = factorial(n)
        message = '''
        <p>dla liczby <b>{}</b></p>
        <br>
        <p>2<sup>{}</sup> = {}</p>
        <p>{}<sup>2</sup> = {}</p>
        <p>{}! = {}</p> 
        '''
        return build_page("Zadanie 1",message.format(n,n,n1,n,n2,n,n3))
    message = '''
    <form method='POST'>
        <input name="n" autofocus placeholder="Podaj liczbę naturalną:" type="number" />
        <input type="submit" value="OK" />
    </form>
    '''
    return build_page("Zadanie 1",message)
