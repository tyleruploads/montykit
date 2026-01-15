# montykit

montykit is an expanding Python library made for a variety of general-purpose purposes. It has NO connection to Monty Pythons Flying Circus or any other packages;
the name was chosen due to to the fact the Python coding language is partially named from Monty Python and his flying circus and is common for general-purpose libraries.

Don't worry, this will be updated a lot! It is only in the very early stages of development!

I made this because I was thinking of a good library to make, and I decided that I needed something very general. I picked a general-purpose library because I want to be able to pack as much high-quality content and modules as possible into it.

---

## Install me!

Install from PyPI:

```bash
pip install montykit
```

## Note:

Feel free to look around the files! If you see anything you think should be added or changed, a suggestion for a new module, a potential bug, or anything, you can email me at tyleruploadspython@gmail.com, tyleruploads@yahoo.com, or make an issue at https://github.com/tyleruploads/montykit/issues. I will try to respond to real emails as fast as possible.

## Text Analysis (`montykit.analysis`)

Utilities for basic text analysis.

```python
from montykit.analysis import (
    text_polarity,
    text_subjectivity,
    word_freq,
    detect_lang,
    text_difficulty,
    text_is_difficult
)

text = """\
Arthur remained very worried.

“But can we trust him?” he said.

“Myself I’d trust him to the end of the Earth,” said Ford.

“Oh yes,” said Arthur, “and how far’s that?”

“About twelve minutes away,” said Ford, “come on, I need a drink.”
"""

text_polarity(text)
text_subjectivity(text)
word_freq(text)
detect_lang(text)
text_difficulty(text)
text_is_difficult(text)
```

---

## Ciphers (`montykit.ciphers`)

Utilities for basic ciphers and encoding methods.

```python
from montykit.ciphers import (
    caesar_cipher,
    rot13,
    atbash_cipher,
    reverse_cipher,
    eng_to_morse,
    morse_to_eng,
    a1z26_cipher,
    bacon_cipher,
    substitution_cipher,
    rail_fence_2_cipher,
    eng_to_imct
)

caesar_cipher("Hello", 3)
caesar_cipher("Khoor", 3, decrypt=True)

rot13("I am a python because I eat coding languages")
atbash_cipher("Antidisestablishmentarianism")
reverse_cipher("Pytondiake")

eng_to_morse("SOS")
morse_to_eng("... --- ...")

a1z26_cipher("This will become nice numbers")

bacon_cipher("This tastes like bacon")

substitution_cipher(text="I am the abc singer in a sing sing lalalalal", alphabet_key="pqrstuvwxyzabcdefghijklmno")

rail_fence_2_cipher("I am both a railing, AND a fence!!")

eng_to_imct("This hopefully is not english, because this was typed on a keyboard!")


```

---

## Converters (`montykit.converters`)

Utilities for basic conversions

```python
from montykit.converters import (
    base64_encode,
    base64_decode,
    text_to_binary,
    binary_to_text,
    text_to_hex,
    hex_to_text,
    text_to_url,
    url_to_text,
    to_snake_case,
    to_camel_case
)

base64_encode("hello")
base64_decode("aGVsbG8=")

text_to_binary("Python")
binary_to_text("01010000 01111001")

text_to_hex("Data")
hex_to_text("44617461")

text_to_url("hello world")
url_to_text("hello%20world")

to_snake_case("CamelCaseText")
to_camel_case("snake_case_text")
```

---

## Generators (`montykit.generator`)

Utilities for basic data/text generation

```python
from montykit.generator import (
    gen_id,
    gen_uuid,
    gen_password,
    gen_first_name,
    gen_first_names,
    gen_full_name,
    gen_phone
)

gen_id()
gen_uuid()
gen_password()

gen_first_name()
gen_first_names(5)

gen_full_name()
gen_full_name(middle=True)

gen_phone()
```

---

## Hashing (`montykit.hash`)

Utilities for basic hashing

```python
from montykit.hash import generate_hash

generate_hash("I am a GIL")
generate_hash("Hopefully I am not a dependancy", algorithm="sha1")
generate_hash("This is NOT a GUI", algorithm="sha256")
```

---

## Validators (`montykit.validators`)

Utilities for basic validation

```python
from montykit.validators import (
    json_validator,
    is_email,
    is_strong_pass
)

json_validator('{"name": "Tyler", "coder": "yes"}')
is_email("tyleruploadspython@gmail.com")
is_strong_pass("W0KZsN1rVzqzha4zvKDgct47SPZgIv2r5ZnD8m3KYyfRRzg35T")
```

---

## Requirements

- Python 3.9 or newer

Dependencies:
- textblob
- textstat

---

## Testing

To ensure the code works, just type pytest while cd'd in the outermost montykit folder.

```bash
pytest
```

---

## License

See "LICENSE" file

---

## Links

- GitHub: https://github.com/tyleruploads/montykit
- Issues: https://github.com/tyleruploads/montykit/issues
