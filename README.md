# BeastPW

BeastPW is a modular password generator for ethical hacking and CTFs.
It builds large wordlists from personal answers, leetspeak, prefixes, suffixes, and random insertions.
Run it in labs and controlled environments only.

## Quick install

```bash
cd beastpw
pip install .
```

## Quick start

```bash
beastpw --config beastpw/config.json --output my_wordlist.txt
```

Options

* --config: path to JSON config file. Default: config.json
* --output: output wordlist file. Default: password_list.txt

## Features

- 20+ invasive questions (skippable).
- L33t mappings (a→4,@, t→7, g→9, b→8, z→2).
- Prefixes (my, super, best) and suffixes (123, !, @).
- Random number/symbol insertions (bl#ue, fi2do).
- Progressive file writing for massive wordlists.
- JSON-driven config for ultimate flexibility.

## Example run

```text
[*] BeastPW v3.0 - LET’S FUCKIN’ DESTROY SHIT!
[*] Yo, spill the dirt or hit Enter to skip, you sneaky bastard!
What's your favorite color? blue
Got a pet? What's its name? fido
First crush's name? jessica
Random word you love? chaos
Favorite animal? dragon
Childhood hero?
[*] Wordlist dumped to my_wordlist.txt. 2048 passwords, you fuckin’ god!
[*] Generated 2048 passwords. Go rule the world (ethically, ya know)!
```

Sample outputs

* blue
* 8lu3
* myblue!
* superf1d0
* bl#ue123
* fido1985
* bluefido@
* jess1c4
* ch4os2025
* dr4g0n!

## Why this project matters

* Installable. Run from anywhere after pip install.
* Config-driven. Adjust behavior without code changes.
* Scalable. Handles large lists without huge RAM use.
* Practical. Useful for CTFs and lab-based security testing.

## Pro tips

- Custom Configs: Create multiple config.json files for different scenarios (e.g., corporate.json, personal.json).
- Extend It: Add more l33t mappings or prefixes in config.json.
- Pair with Tools: Use with Hashcat or John the Ripper for lab testing.
- Ethical Use: Keep it in CTFs or labs. Real-world misuse is a one-way ticket to fucksville.

## Ethics

 Ethical Use: Keep it in CTFs or labs. Real-world misuse is a one-way ticket to fucksville.


