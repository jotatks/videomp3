<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Baixar YouTube MP3</title>
</head>
<body>
    <h1>Conversor YouTube → MP3</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Cole o link do YouTube aqui" required>
        <button type="submit">Converter</button>
    </form>

    {% if error %}
        <p style="color: red;">Erro: {{ error }}</p>
    {% endif %}

    {% if success %}
        <p>Playlist baixada com sucesso!</p>
        <ul>
            {% for file in files %}
                <li><a href="{{ file }}">Baixar arquivo {{ loop.index }}</a></li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
