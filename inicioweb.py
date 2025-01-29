from flask import Flask, render_template_string

import pandas as pd

app = Flask(__name__)

df = pd.read_csv('datacleaning.csv')
df = df.dropna()#esse método é para retirar as células (valores) vazios

df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False)#esse método é para corrigir valores de datas mal 
#formatados.

df.loc[7, 'Duration'] = 45 #esse método é para corrigir valores com erro de digitação. Erros do tipo "typo", in english.

df.drop_duplicates(inplace=True)

@app.route('/')

def show_data():
    table_html = df.to_html(classes='table table-striped', index=False)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dados com Pandas</title>
        <link rel="stylesheet" 
              href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1>Dados do Arquivo JSON</h1>
            {table_html}
        </div>
    </body>
    </html>
    """

    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)