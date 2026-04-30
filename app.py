from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Docker — TOMBI Jacky</title>
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg: #060a10;
            --surface: #0d1420;
            --border: rgba(255,255,255,0.07);
            --accent: #00e5ff;
            --accent2: #7c3aed;
            --text: #e2e8f0;
            --muted: #64748b;
        }

        body {
            font-family: 'DM Sans', sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }

        /* Fond animé */
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background:
                radial-gradient(ellipse 60% 50% at 20% 20%, rgba(0,229,255,0.08) 0%, transparent 60%),
                radial-gradient(ellipse 50% 60% at 80% 80%, rgba(124,58,237,0.1) 0%, transparent 60%);
            pointer-events: none;
            animation: pulse-bg 8s ease-in-out infinite alternate;
        }

        @keyframes pulse-bg {
            from { opacity: 0.6; }
            to   { opacity: 1; }
        }

        /* Grille décorative */
        body::after {
            content: '';
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
            background-size: 60px 60px;
            pointer-events: none;
        }

        .container {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 680px;
            padding: 24px;
        }

        /* Carte principale */
        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 52px 56px;
            position: relative;
            overflow: hidden;
            animation: slide-in 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;
        }

        @keyframes slide-in {
            from { opacity: 0; transform: translateY(30px) scale(0.97); }
            to   { opacity: 1; transform: translateY(0) scale(1); }
        }

        /* Trait lumineux en haut */
        .card::before {
            content: '';
            position: absolute;
            top: 0; left: 10%; right: 10%;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--accent), var(--accent2), transparent);
        }

        /* Blob décoratif dans la carte */
        .card::after {
            content: '';
            position: absolute;
            width: 300px; height: 300px;
            background: radial-gradient(circle, rgba(0,229,255,0.04) 0%, transparent 70%);
            top: -100px; right: -100px;
            border-radius: 50%;
            pointer-events: none;
        }

        .header {
            display: flex;
            align-items: center;
            gap: 18px;
            margin-bottom: 40px;
        }

        .whale {
            font-size: 52px;
            line-height: 1;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50%       { transform: translateY(-8px); }
        }

        .header-text h1 {
            font-family: 'Syne', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 30%, var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1;
        }

        .header-text p {
            font-size: 0.85rem;
            color: var(--muted);
            margin-top: 4px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }

        .divider {
            height: 1px;
            background: var(--border);
            margin: 0 0 36px;
        }

        .message {
            font-size: 1.1rem;
            color: #94a3b8;
            line-height: 1.8;
            margin-bottom: 36px;
        }

        .message strong {
            color: var(--text);
            font-weight: 500;
        }

        /* Badges de statut */
        .badges {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 100px;
            font-size: 0.78rem;
            font-weight: 500;
            letter-spacing: 0.03em;
            border: 1px solid;
            animation: fade-up 0.5s ease both;
        }

        .badge:nth-child(1) { animation-delay: 0.3s; }
        .badge:nth-child(2) { animation-delay: 0.45s; }
        .badge:nth-child(3) { animation-delay: 0.6s; }

        @keyframes fade-up {
            from { opacity: 0; transform: translateY(10px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .badge-green {
            color: #34d399;
            border-color: rgba(52,211,153,0.25);
            background: rgba(52,211,153,0.06);
        }

        .badge-blue {
            color: var(--accent);
            border-color: rgba(0,229,255,0.25);
            background: rgba(0,229,255,0.06);
        }

        .badge-purple {
            color: #a78bfa;
            border-color: rgba(167,139,250,0.25);
            background: rgba(167,139,250,0.06);
        }

        .dot {
            width: 6px; height: 6px;
            border-radius: 50%;
            background: currentColor;
            animation: blink 1.4s ease-in-out infinite;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50%       { opacity: 0.3; }
        }

        /* Infos techniques */
        .tech-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .tech-item {
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 18px;
            animation: fade-up 0.5s ease both;
        }

        .tech-item:nth-child(1) { animation-delay: 0.5s; }
        .tech-item:nth-child(2) { animation-delay: 0.6s; }
        .tech-item:nth-child(3) { animation-delay: 0.7s; }
        .tech-item:nth-child(4) { animation-delay: 0.8s; }

        .tech-label {
            font-size: 0.7rem;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 4px;
        }

        .tech-value {
            font-family: 'Syne', sans-serif;
            font-size: 0.95rem;
            color: var(--text);
        }

        /* Pied de carte */
        .footer {
            margin-top: 36px;
            padding-top: 24px;
            border-top: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.78rem;
            color: var(--muted);
        }

        .footer .author {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .avatar {
            width: 28px; height: 28px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--accent), var(--accent2));
            display: flex; align-items: center; justify-content: center;
            font-size: 0.7rem;
            font-weight: 700;
            color: var(--bg);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">

            <div class="header">
                <div class="whale">🐳</div>
                <div class="header-text">
                    <h1>Bonjour à tous !</h1>
                    <p>Application conteneurisée avec Docker</p>
                </div>
            </div>

            <div class="divider"></div>

            <p class="message">
                Ceci est une application <strong>Flask</strong> simple,
                déployée à l'intérieur d'un conteneur <strong>Docker</strong>.<br>
                Elle illustre les concepts de base : <strong>Dockerfile</strong>,
                <strong>image</strong> et <strong>conteneur</strong>.
            </p>

            <div class="badges">
                <span class="badge badge-green">
                    <span class="dot"></span> Conteneur actif
                </span>
                <span class="badge badge-blue">
                    🐍 Python 3.9
                </span>
                <span class="badge badge-purple">
                    ⚡ Flask
                </span>
            </div>

            <div class="tech-grid">
                <div class="tech-item">
                    <div class="tech-label">Image de base</div>
                    <div class="tech-value">python:3.9</div>
                </div>
                <div class="tech-item">
                    <div class="tech-label">Port exposé</div>
                    <div class="tech-value">5000</div>
                </div>
                <div class="tech-item">
                    <div class="tech-label">Répertoire</div>
                    <div class="tech-value">/app</div>
                </div>
                <div class="tech-item">
                    <div class="tech-label">Hôte</div>
                    <div class="tech-value">0.0.0.0</div>
                </div>
            </div>

            <div class="footer">
                <span>KEYCE — CC1 DevOps 2026</span>
                <div class="author">
                    <div class="avatar">MN</div>
                    <span>Réalisé par <strong style="color: var(--text);">mon_nom</strong></span>
                </div>
            </div>

        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

