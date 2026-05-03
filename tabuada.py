from typing import Optional

from flask import Flask, request

app = Flask(__name__)


def _render(n: Optional[int] = None, error: Optional[str] = None) -> str:
    tabuada_html = ""
    pares_html = ""

    if n is not None:
        tabuada_html = "\n".join(
            f"<li>{n} x {i} = <strong>{n * i}</strong></li>" for i in range(1, 11)
        )
        pares_html = "\n".join(
            f"<li>contador={i} → <strong>{i * 2}</strong></li>" for i in range(1, 11)
        )

    error_html = f"<p class='erro'>{error}</p>" if error else ""

    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Tabuada</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Arial, sans-serif; background: #f6f6f6; }}
    .caixa {{
      max-width: 520px;
      margin: 40px auto;
      padding: 16px;
      background: #fff;
      border: 1px solid #ddd;
      border-radius: 8px;
    }}
    h1 {{ margin: 0 0 12px; font-size: 18px; }}
    form {{ display: flex; gap: 8px; margin-bottom: 12px; }}
    input {{
      flex: 1;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 6px;
      outline: none;
    }}
    button {{
      padding: 10px 12px;
      border: 1px solid #ddd;
      background: #fff;
      border-radius: 6px;
      cursor: pointer;
    }}
    .erro {{
      margin: 0 0 12px;
      padding: 10px;
      background: #fff2f2;
      border: 1px solid #ffd6d6;
      border-radius: 6px;
      color: #a40000;
    }}
    .bloco {{
      margin-top: 12px;
      padding: 12px;
      background: #fafafa;
      border: 1px solid #e5e5e5;
      border-radius: 6px;
    }}
    .bloco h2 {{ margin: 0 0 8px; font-size: 14px; }}
    ul {{ margin: 0; padding-left: 18px; }}
    li {{ margin: 6px 0; }}
  </style>
</head>
<body>
  <div class="caixa">
    <h1>Tabuada (for) + Pares (while)</h1>
    <form method="get" action="/">
      <input name="n" type="number" placeholder="Digite um número" value="{'' if n is None else n}" required />
      <button type="submit">Gerar</button>
    </form>
    {error_html}
    <div class="bloco">
      <h2>Utilizando for: Tabuada do número</h2>
      <ul>
        {tabuada_html}
      </ul>
    </div>
    <div class="bloco">
      <h2>Utilizando while: contador é definido como 1 e multiplicado por 2</h2>
      <ul>
        {pares_html}
      </ul>
    </div>
  </div>
</body>
</html>
"""


@app.get("/")
def index():
    n_raw = request.args.get("n", "").strip()
    if not n_raw:
        return _render()

    try:
        n = int(n_raw)
    except ValueError:
        return _render(error="Digite um número inteiro válido."), 400

    return _render(n=n)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
