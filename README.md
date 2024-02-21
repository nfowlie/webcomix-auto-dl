# webcomix-auto-dl

An extension of J-CPelletier/webcomix that allows for bulk download of comics based on a YAML file

## Instructions

- Install [Python 3](https://www.python.org/downloads/)
- Install [J-CPelletier's Webcomix](https://github.com/J-CPelletier/webcomix)
- Download webcomix-auto-dl.py
- Run webcomix-auto-dl.py

## Example YAML

```yaml
comics:
  egs:
    name: "El Goonish Shive"
    nextPage: "//a[@rel='next']/@href"
    image: "//img[@id='cc-comic']/@src"
    volumes:
      1:
        name: "El Goonish Shive"
        vol: "1"
        chapters:
          1:
            name: "Introductions"
            startURL: "https://www.egscomics.com/comic/2002-01-21"
            endURL: "https://www.egscomics.com/comic/2002-01-27"
            ch: "1"
          2:
            name: "The Goo"
            startURL: "https://www.egscomics.com/comic/2002-01-28"
            endURL: "https://www.egscomics.com/comic/2002-02-10"
            ch: "2"
      2:
        name: "Sister"
        vol: "2"
        chapters:
          1:
            name: "Open The Box Part 1"
            startURL: "https://www.egscomics.com/comic/2002-05-26"
            endURL: "https://www.egscomics.com/comic/2002-06-04"
            ch: "1"
  ggr:
    name: "Go Get a Roomie!"
    nextPage: "//a[@rel='next']/@href"
    image: "//img[@id='cc-comic']/@src"
    volumes:
      1:
        name: "Book One"
        vol: "1"
        chapters:
          1:
            name: "Meet Roomie!"
            startURL: "https://www.gogetaroomie.com/comic/and-so-it-begins"
            endURL: "https://www.gogetaroomie.com/comic/ends-with-a-kiss"
            ch: "1"
          2:
            name: "Pillow Love"
            startURL: "https://www.gogetaroomie.com/comic/flash-those-tits"
            endURL: "https://www.gogetaroomie.com/comic/merry-charism-ass"
            ch: "2"
```
