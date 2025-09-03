# KRISPER Demo Script (30 seconds)

## Screen Recording Script

1. **Open terminal** (0-3s)
   ```bash
   $ python3
   >>> from krisper import compile_text
   ```

2. **Type in plain English** (3-10s)
   ```python
   >>> compile_text("compress file 'data.txt' as backup")
   ```

3. **Show the output** (10-15s)
   ```json
   {
     "plan": [{"op": "compress", "in": {"file": "data.txt"}, "out": "backup"}]
   }
   ```

4. **Run Bio_Poetica poem** (15-25s)
   ```bash
   $ python3 simple_demo.py
   ```
   Show the poetry → code transformation

5. **End card** (25-30s)
   "Programming without syntax.
   github.com/echo313unfolding/KRISPER"

## Recording Tips
- Use asciinema or terminalizer
- Keep it under 30 seconds
- Big, readable font
- Dark theme