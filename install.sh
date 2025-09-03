#!/bin/bash
# Quick install script for KRISPER demos

echo "🧬 Installing KRISPER demos..."

# Create symlinks in ~/bin
mkdir -p ~/bin

# Make scripts executable
chmod +x simple_demo.py
chmod +x live_demo.py
chmod +x krisper_executor.py

# Create wrapper scripts
echo '#!/bin/bash
python3 ~/krisper_github/simple_demo.py' > ~/bin/krisper-demo
chmod +x ~/bin/krisper-demo

echo '#!/bin/bash
python3 ~/krisper_github/live_demo.py' > ~/bin/krisper-live
chmod +x ~/bin/krisper-live

echo "✅ Installation complete!"
echo ""
echo "You can now run from anywhere:"
echo "  krisper-demo    # See the magic"
echo "  krisper-live    # Interactive demo"
echo ""
echo "Or navigate to: cd ~/krisper_github"