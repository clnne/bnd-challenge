# Kommandos zur Lösung

```bash
./decrypt.py
```

```bash
~/Software/john/run/zip2john geheim.zip > zip.hash
```

```bash
~/Software/john/run/john zip.hash --wordlist=/usr/share/wordlists/rockyou.txt

~/Software/john/run/john zip.hash --show
```

```bash
unzip -P roneisha2209 geheim.zip
```

```bash
~/Software/john/run/keepass2john verwahrgelass.kdbx > keepass.hash
```

```bash
~/Software/john/run/john keepass.hash --wordlist=/usr/share/wordlists/rockyou.txt
```