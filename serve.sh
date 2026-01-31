#!/bin/bash
# Local MkDocs Server for VibeLearning
# Usage: ./serve.sh [port]

set -e

# Default port
PORT=${1:-8000}

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  VibeLearning - Local MkDocs Server${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment not found. Creating one...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi

# Activate virtual environment
echo -e "${BLUE}Activating virtual environment...${NC}"
source venv/bin/activate

# Check if dependencies are installed
if ! pip show mkdocs-material &>/dev/null; then
    echo -e "${YELLOW}Installing dependencies...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}✓ Dependencies installed${NC}"
fi

echo ""
echo -e "${GREEN}✓ Virtual environment activated${NC}"
echo -e "${GREEN}✓ Dependencies ready${NC}"
echo ""

# Check if docs directory exists
if [ ! -d "docs" ]; then
    echo -e "${YELLOW}Setting up docs directory for local testing...${NC}"
    mkdir -p docs
    cp README.md docs/
    cp -r [0-9]* docs/ 2>/dev/null || true
    cp -r Resources docs/ 2>/dev/null || true
    cp -r stylesheets docs/ 2>/dev/null || true
    cp -r overrides docs/ 2>/dev/null || true
    echo -e "${GREEN}✓ Docs directory created${NC}"
fi

echo ""
echo -e "${BLUE}Starting MkDocs server...${NC}"
echo -e "${YELLOW}Server will be available at:${NC}"
echo -e "  ${GREEN}http://127.0.0.1:${PORT}/VibeLearning/${NC}"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop the server${NC}"
echo ""

# Start the server
mkdocs serve --dev-addr=127.0.0.1:${PORT}
