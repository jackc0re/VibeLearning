#!/bin/bash
# Clean build artifacts and temporary files
# Usage: ./clean.sh

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  VibeLearning - Clean Build Artifacts${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Remove build directories
echo -e "${YELLOW}Removing build directories...${NC}"
rm -rf site
rm -rf docs
rm -rf vibelearning-site
echo -e "${GREEN}✓ Removed site/ docs/ vibelearning-site/${NC}"

# Remove Python cache
echo -e "${YELLOW}Removing Python cache...${NC}"
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
echo -e "${GREEN}✓ Removed Python cache${NC}"

# Remove backup files
echo -e "${YELLOW}Removing backup files...${NC}"
rm -f mkdocs.yml.local
echo -e "${GREEN}✓ Removed backup files${NC}"

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  ✓ Cleanup complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${YELLOW}Note: Virtual environment (venv/) preserved${NC}"
echo -e "To remove venv as well, run: ${BLUE}rm -rf venv/${NC}"
