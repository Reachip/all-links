# all_links : Get all links of a website

The all_links CLI let you get all links of a given website.
The output can be generated in three ways: to JSON, to XML or printed to from terminal (stdout).

## Positional arguments

url => The website URL (ex: https://reachip.github.io)
output => Output : xml - json - stdout

## Optional arguments

-h, --help           display help message
--filename FILENAME  output filename if you want to generate a JSON or XML format 

## Example

```
python -m all_links https://reachip.github.io xml --filename=mywebsite
```

Next, the program generate a XML file named ```mywebsite.xml``` like that : 

```xml
<urls>
    <annexe>
        <link>https://reachip.github.io/annexe/CV.html#CV</link>
        <link>https://reachip.github.io/annexe/tmp.html#tmp</link>
        <link>https://reachip.github.io/annexe/projets-scolaires.html#projets-scolaires</link>
    </annexe>
    <articles>
        <link>https://reachip.github.io/articles/fr/resoudre-erreur-ENOSPC-expo-react-native.html#resoudre-erreur-ENOSPC-expo-react-native</link>
        <link>https://reachip.github.io/articles/fr/python-asynchronisme-par-la-pratique.html#python-asynchronisme-par-la-pratique</link>
        <link>https://reachip.github.io/articles/fr/asynchronisme-avec-python.html#asynchronisme-avec-python</link>
        <link>https://reachip.github.io/articles/fr/creer-blog-pelican.html#creer-blog-pelican</link>
        <link>https://reachip.github.io/articles/fr/read-the-fucking-manual.html#read-the-fucking-manual</link>
        <link>https://reachip.github.io/articles/fr/programmer-ou-coder.html#programmer-ou-coder</link>
        <link>https://reachip.github.io/articles/fr/regrettez-vous-etre-devenu-ing\xc3\xa9nieur-pourquoi-quora.html#regrettez-vous-etre-devenu-ing\xc3\xa9nieur-pourquoi-quora</link>
        <link>https://reachip.github.io/articles/fr/passage-argument-rust.html#passage-argument-rust</link>
        <link>https://reachip.github.io/articles/fr/lifetime-langage-rust.html#lifetime-langage-rust</link>
    </articles>
    <category>
        <link>https://reachip.github.io/category/js.html</link>
        <link>https://reachip.github.io/category/python.html</link>
        <link>https://reachip.github.io/category/programmation.html</link>
        <link>https://reachip.github.io/category/quora.html</link>
        <link>https://reachip.github.io/category/rust.html</link>
    </category>
    <tag>
        <link>https://reachip.github.io/tag/js.html</link>
        <link>https://reachip.github.io/tag/tuto.html</link>
        <link>https://reachip.github.io/tag/expo.html</link>
        <link>https://reachip.github.io/tag/react-native.html</link>
        <link>https://reachip.github.io/tag/python.html</link>
        <link>https://reachip.github.io/tag/asyncio.html</link>
        <link>https://reachip.github.io/tag/gitbook.html</link>
        <link>https://reachip.github.io/tag/sti2d.html</link>
        <link>https://reachip.github.io/tag/random.html</link>
        <link>https://reachip.github.io/tag/opinion.html</link>
        <link>https://reachip.github.io/tag/quora.html</link>
        <link>https://reachip.github.io/tag/programmation.html</link>
        <link>https://reachip.github.io/tag/rust.html</link>
        <link>https://reachip.github.io/tag/idees.html</link>
        <link>https://reachip.github.io/tag/these.html</link>
    </tag><>
    <link>https://reachip.github.io/</link>
</urls>
<lasynchronisme-avec-python.html>
    <link>https://reachip.github.io/lasynchronisme-avec-python.html</link>
</lasynchronisme-avec-python.html>
</urls>
```

## Installation

```
pip install -r requirements
```
