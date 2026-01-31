#!/bin/bash
# Build VibeLearning documentation locally
# Usage: ./build.sh

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  VibeLearning - Build Documentation${NC}"
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

echo -e "${GREEN}✓ Virtual environment activated${NC}"
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

# Clean previous build
echo -e "${BLUE}Cleaning previous build...${NC}"
rm -rf site
echo -e "${GREEN}✓ Cleaned${NC}"
echo ""

# Build the documentation
echo -e "${BLUE}Building documentation...${NC}"
if mkdocs build; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}  ✓ Build successful!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo -e "${BLUE}Site built in:${NC} ./site/"
    echo ""
    echo -e "${YELLOW}To view locally, run:${NC}"
    echo -e "  ${GREEN}./serve.sh${NC}"
    echo ""
    echo -e "${YELLOW}Or open:${NC}"
    echo -e "  ${GREEN}file://$(pwd)/site/index.html${NC}"
else
    echo ""
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}  ✗ Build failed!${NC}"
    echo -e "${RED}========================================${NC}"
    exit 1
fi
