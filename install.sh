#!/bin/bash

# =========================================
# 🎤 VoiceClone Studio - Script d'installation
# =========================================

echo "🎤 VoiceClone Studio - Installation"
echo "===================================="
echo ""

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Vérifie Python
echo -e "${BLUE}[1/5]${NC} Vérification de Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION trouvé"
else
    echo -e "${RED}✗${NC} Python 3 non trouvé. Installe Python 3.11+ d'abord."
    exit 1
fi

# Crée l'environnement virtuel
echo ""
echo -e "${BLUE}[2/5]${NC} Création de l'environnement virtuel..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} Environnement virtuel créé"
else
    echo -e "${YELLOW}!${NC} Environnement virtuel existant"
fi

# Active l'environnement
echo ""
echo -e "${BLUE}[3/5]${NC} Activation de l'environnement..."
source venv/bin/activate
echo -e "${GREEN}✓${NC} Environnement activé"

# Mise à jour pip
echo ""
echo -e "${BLUE}[4/5]${NC} Mise à jour de pip..."
pip install --upgrade pip -q
echo -e "${GREEN}✓${NC} pip mis à jour"

# Installation des dépendances
echo ""
echo -e "${BLUE}[5/5]${NC} Installation des dépendances..."
echo "    Cela peut prendre quelques minutes..."

# Détecte le système
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS - vérifie si Apple Silicon
    if [[ $(uname -m) == "arm64" ]]; then
        echo -e "${YELLOW}!${NC} Mac Apple Silicon détecté - Installation optimisée MPS"
        pip install torch torchaudio -q
    else
        echo -e "${YELLOW}!${NC} Mac Intel détecté"
        pip install torch torchaudio -q
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux - vérifie CUDA
    if command -v nvidia-smi &> /dev/null; then
        echo -e "${YELLOW}!${NC} GPU NVIDIA détecté - Installation CUDA"
        pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu124 -q
    else
        echo -e "${YELLOW}!${NC} Pas de GPU NVIDIA - Installation CPU"
        pip install torch torchaudio -q
    fi
else
    # Windows ou autre
    pip install torch torchaudio -q
fi

# Installe le reste
pip install -r requirements.txt -q

echo -e "${GREEN}✓${NC} Dépendances installées"

# Termine
echo ""
echo "===================================="
echo -e "${GREEN}✓ Installation terminée !${NC}"
echo ""
echo "Pour lancer l'application :"
echo ""
echo -e "  ${BLUE}source venv/bin/activate${NC}"
echo -e "  ${BLUE}streamlit run app.py${NC}"
echo ""
echo "L'app s'ouvrira sur http://localhost:8501"
echo "===================================="
