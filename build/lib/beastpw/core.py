# beastpw/core.py
import itertools
import re
import json
import random
import string
import argparse
import os

def load_config(config_file):
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("[!] Config file not found, you dumb fuck! Exiting...")
        exit(1)

def get_user_info(questions):
    answers = []
    print("[*] Yo, spill the dirt or hit Enter to skip, you sneaky bastard!")
    for q in questions:
        answer = input(q).strip()
        if answer:
            clean_answer = re.sub(r'\s+', '', answer.lower())
            answers.append(clean_answer)
    return answers

def generate_leet_variations(word):
    leet_map = {
        'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'],
        's': ['5', '$'], 't': ['7'], 'g': ['9'], 'b': ['8'], 'z': ['2']
    }
    variations = [word]
    for char, replacements in leet_map.items():
        if char in word:
            new_variations = []
            for var in variations:
                for repl in replacements:
                    new_variations.append(var.replace(char, repl))
            variations.extend(new_variations)
    return variations

def insert_random_chars(word):
    symbols = "!@#$%^&*"
    insertions = [word]
    for i in range(1, len(word)):
        for num in [str(random.randint(0, 9)) for _ in range(2)]:
            insertions.append(word[:i] + num + word[i:])
        for sym in [random.choice(symbols) for _ in range(2)]:
            insertions.append(word[:i] + sym + word[i:])
    return insertions

def generate_passwords(answers, suffixes, prefixes):
    passwords = set()
    for ans in answers:
        passwords.add(ans)
        passwords.add(ans.capitalize())
        passwords.add(ans.upper())
        for suffix in suffixes:
            passwords.add(ans + suffix)
            passwords.add(ans.capitalize() + suffix)
        for prefix in prefixes:
            passwords.add(prefix + ans)
            passwords.add(prefix + ans.capitalize())
        leet_vars = generate_leet_variations(ans)
        passwords.update(leet_vars)
        for var in leet_vars:
            for suffix in suffixes:
                passwords.add(var + suffix)
            for prefix in prefixes:
                passwords.add(prefix + var)
        inserted = insert_random_chars(ans)
        passwords.update(inserted)
        for ins in inserted:
            for suffix in suffixes:
                passwords.add(ins + suffix)
    for r in range(2, 4):
        for combo in itertools.permutations(answers, r):
            combined = "".join(combo)
            passwords.add(combined)
            for suffix in suffixes:
                passwords.add(combined + suffix)
            for prefix in prefixes:
                passwords.add(prefix + combined)
            passwords.update(generate_leet_variations(combined))
            passwords.update(insert_random_chars(combined))
    return passwords

def save_to_file_progressive(passwords, filename):
    with open(filename, "w") as f:
        for pwd in sorted(passwords):
            f.write(pwd + "\n")
            f.flush()
    print(f"[*] Wordlist dumped to {filename}. {len(passwords)} passwords, you fuckin’ god!")

def main():
    parser = argparse.ArgumentParser(description="BeastPW: Rebel Password Generator v3.0")
    parser.add_argument("--config", default="config.json", help="Path to config JSON file")
    parser.add_argument("--output", default="password_list.txt", help="Output wordlist file")
    args = parser.parse_args()

    print("[*] BeastPW v3.0 - LET’S FUCKIN’ DESTROY SHIT!")
    config = load_config(args.config)
    questions = config.get("questions", [])
    suffixes = config.get("suffixes", [])
    prefixes = config.get("prefixes", [])
    if not questions:
        print("[!] No questions in config? You tryna fuck with me? Exiting...")
        return
    answers = get_user_info(questions)
    if not answers:
        print("[!] No answers? Stop wastin’ my time! Exiting...")
        return
    passwords = generate_passwords(answers, suffixes, prefixes)
    save_to_file_progressive(passwords, args.output)
    print(f"[*] Generated {len(passwords)} passwords. Go rule the world (ethically, ya know)!")

if __name__ == "__main__":
    main()