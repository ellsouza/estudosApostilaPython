# Importa a biblioteca Flask
from datetime import datetime

from flask import Flask, jsonify

# Cria a aplicação
app = Flask(__name__)

# Cria a rota /automacao
@app.route("/")
def inicio():
    # Retorna um texto para o HTML
    return """ <!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Automação com Python</title>
    <style>
      body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #dbeafe, #eff6ff);
        min-height: 100vh;
      }
      .pagina {
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 24px;
        box-sizing: border-box;
      }
      .caixa {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
        text-align: center;
        width: 520px;
        max-width: 100%;
      }
      h1 {
        color: #1d4ed8;
        margin: 0 0 10px;
      }
      p {
        color: #475569;
      }
      button {
        display: block;
        background: #2563eb;
        color: white;
        border: none;
        padding: 12px 18px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
        margin: 15px auto 0;
        width: 220px;
        max-width: 100%;
      }
      button:hover {
        background: #1e40af;
      }
      .bloco {
        margin-top: 14px;
        padding: 12px;
        background: #fafafa;
        border: 1px solid #e5e5e5;
        border-radius: 10px;
        text-align: left;
      }
      .bloco h2 {
        margin: 0 0 8px;
        font-size: 14px;
        color: #1d4ed8;
      }
      #resultado {
        margin: 0;
        white-space: pre-wrap;
        word-break: break-word;
      }
      footer {
        margin-top: 20px;
        text-align: center;
        color: #475569;
        font-size: 14px;
      }
      footer a {
        color: #1d4ed8;
        text-decoration: none;
        font-weight: bold;
      }
      @media (max-width: 560px) {
        .caixa {
          padding: 22px;
        }
      }
    </style>
  </head>
  <body>
    <div class="pagina">
      <div class="caixa">
        <h1>Minha automação</h1>
        <p>Clique para executar a rota <strong>/automacao</strong> no seu Flask.</p>

        <button type="button" onclick="executarAutomacao()">Executar automação</button>

        <div class="bloco" aria-live="polite">
          <h2>Resultado</h2>
          <p id="resultado">Aguardando...</p>
        </div>

        <div class="bloco">
          <h2>O que aconteceu (passo a passo)</h2>
          <ol id="detalhes-list"></ol>
        </div>

        <noscript>
          <p class="bloco" style="border-color:#ffd6d6;background:#fff2f2;color:#a40000;">
            Ative o JavaScript para executar a automação.
          </p>
        </noscript>
      </div>

      <footer>
        Desenvolvido por
        <a href="https://ellsouza.github.io/ellen-portfolio/" target="_blank" rel="noopener noreferrer">Ellen Souza</a>
      </footer>
    </div>

    <script>
      async function executarAutomacao() {
        const resultadoEl = document.getElementById("resultado");
        const detalhesList = document.getElementById("detalhes-list");

        resultadoEl.innerText = "Executando...";
        detalhesList.innerHTML = "";

        try {
          const resposta = await fetch("/automacao");
          const data = await resposta.json();

          resultadoEl.innerText = data.mensagem || "Concluído.";

          (data.detalhes || []).forEach((item) => {
            const li = document.createElement("li");
            li.innerText = item;
            detalhesList.appendChild(li);
          });
        } catch (err) {
          resultadoEl.innerText = "Erro ao conectar no Flask. Confira se está rodando em http://127.0.0.1:5000";
        }
      }
    </script>
  </body>
</html>"""

@app.route("/automacao")
def automacao():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    detalhes = [
        "Você clicou no botão “Executar automação”.",
        "O JavaScript (o código do navegador) pediu ajuda para o Python na rota /automacao.",
        "O Flask recebeu esse pedido e executou a função automacao().",
        "O Python devolveu uma resposta com a mensagem e esta lista de passos.",
        f"Horário em que isso aconteceu: {agora}.",
    ]

    return jsonify(
        mensagem="A automação em Python foi executada com sucesso!",
        detalhes=detalhes,
    )

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)
