# 🎤 VoiceClone Studio

**Clone ta voix localement avec l'IA** - 100% privé, aucune donnée envoyée à des serveurs externes.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)

## ✨ Fonctionnalités

- 🎙️ **Clonage de voix** avec seulement ~10 secondes d'audio
- 🌍 **23 langues** supportées (FR, EN, DE, ES, IT, etc.)
- 🔒 **100% local** - aucune donnée envoyée
- ⚡ **Temps réel** sur GPU (CUDA/MPS)
- 🎛️ **Paramètres ajustables** (émotion, fidélité, créativité)
- 🎨 **Interface moderne** et intuitive

## 🚀 Installation rapide

### Option 1 : Script automatique (Mac/Linux)

```bash
chmod +x install.sh
./install.sh
```

### Option 2 : Installation manuelle

```bash
# Crée un environnement virtuel (Python 3.11 recommandé)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# Installe PyTorch selon ton système
# Mac Apple Silicon:
pip install torch torchaudio

# Linux avec NVIDIA GPU:
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu124

# CPU seulement:
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu

# Installe les autres dépendances
pip install -r requirements.txt
```

## 🎯 Utilisation

```bash
# Active l'environnement
source venv/bin/activate

# Lance l'application
streamlit run app.py
```

L'application s'ouvre automatiquement sur `http://localhost:8501`

## 📖 Guide d'utilisation

### Étape 1 : Prépare ton échantillon audio

- **Durée** : 5-15 secondes
- **Qualité** : Voix claire, sans bruit de fond
- **Format** : WAV, MP3, M4A, OGG, FLAC
- **Conseil** : Parle naturellement avec expression

### Étape 2 : Entre ton texte

Écris le texte que tu veux faire prononcer par ta voix clonée (max 1000 caractères).

### Étape 3 : Ajuste les paramètres (optionnel)

- **Exagération** : 0 = monotone, 1 = très expressif
- **Fidélité** : Plus haut = plus proche de ta voix
- **Créativité** : Variation dans la prononciation

### Étape 4 : Génère !

Clique sur "Cloner ma voix" et attends quelques secondes.

## 🎛️ Paramètres avancés

| Paramètre | Défaut | Description |
|-----------|--------|-------------|
| `exaggeration` | 0.5 | Intensité émotionnelle (0-1) |
| `cfg_weight` | 0.5 | Fidélité à la voix de référence (0-1) |
| `temperature` | 0.8 | Créativité de la génération (0.1-1.5) |

## 🌍 Langues supportées

| Code | Langue | Code | Langue |
|------|--------|------|--------|
| `fr` | 🇫🇷 Français | `ja` | 🇯🇵 日本語 |
| `en` | 🇬🇧 English | `ko` | 🇰🇷 한국어 |
| `de` | 🇩🇪 Deutsch | `zh` | 🇨🇳 中文 |
| `es` | 🇪🇸 Español | `ar` | 🇸🇦 العربية |
| `it` | 🇮🇹 Italiano | `hi` | 🇮🇳 हिन्दी |
| `pt` | 🇵🇹 Português | `tr` | 🇹🇷 Türkçe |
| `nl` | 🇳🇱 Nederlands | `ru` | 🇷🇺 Русский |
| `pl` | 🇵🇱 Polski | `sv` | 🇸🇪 Svenska |

Et plus encore : da, fi, no, el, he, ms, sw

## 💻 Configuration requise

- **Python** : 3.11+ (recommandé)
- **RAM** : 8 GB minimum
- **GPU** (optionnel mais recommandé) :
  - NVIDIA avec CUDA 11.8+
  - Apple Silicon (M1/M2/M3/M4)

## 🐛 Résolution de problèmes

### "ModuleNotFoundError: No module named 'chatterbox'"

```bash
pip install chatterbox-tts
```

### "CUDA out of memory"

Réduis la longueur du texte ou utilise le CPU.

### "MPS backend out of memory" (Mac)

```bash
export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0
```

### L'audio généré est de mauvaise qualité

- Utilise un échantillon audio plus long (10-15s)
- Assure-toi qu'il n'y a pas de bruit de fond
- Ajuste les paramètres de fidélité

## 📁 Structure du projet

```
voice_cloner/
├── app.py              # Application Streamlit principale
├── requirements.txt    # Dépendances Python
├── install.sh          # Script d'installation
└── README.md           # Ce fichier
```

## 🙏 Crédits

- **Chatterbox TTS** par [Resemble AI](https://github.com/resemble-ai/chatterbox)
- **Streamlit** pour l'interface web
- **PyTorch** pour le deep learning

## 📄 License

MIT License - Utilisation libre pour projets personnels et commerciaux.

---

Fait avec ❤️ par VoiceClone Studio
