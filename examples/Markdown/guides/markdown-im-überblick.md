# Markdown im Überblick

Das vorliegende Dokument ist ein Beispiel-Dokument für die wichtigsten Aspekte der Markdown-Syntax. Für viele weitere Hinweise empfiehlt sich das Buch von Michael Kofler, *Markdown und Pandoc* (Graz: ebooks.kofler, 2018), URL: https://kofler.info/ebooks/markdown_pandoc/.

# Grundlagen

## Absätze

Absätze werden einfach durch eine Leerzeile markiert.

Hier folgt also jetzt der zweite Absatz. Mehrere Leerzeilen werden als eine Absatzgrenze interpretiert.

Sie sollten Markdown-Dateien immer in UTF-8 abspeichern (vor allem unter Windows ist das wichtig und muss aktiviert werden.)


## Überschrift (zweiter Ordnung)

Überschriften werden mit einem oder mehreren `#` markiert.

### Überschrift (dritter Ordnung)

Hier findet man Text. Das geht auch noch so weiter, bis zur 5. Überschriftenebene. Die exakte Darstellung der Überschriften lässt sich, wie sehr vieles, über CSS bei der Transformation steuern.


## Hervorhebungen von Text

Das hier ist ein normaler Text, in dem einige *Wörter* durch Kursivierung oder durch Fettdruck besonders **hervorgehoben** sind.

Das geht entweder mit dem Asterisk `*`, oder aber mit dem Underscore `_`. Das sieht für _hervorgehobene_ Worte dann eben __so wie hier gezeigt__ aus.

Um dafür zu sorgen, dass reservierte Zeichen von Markdown wie das Asterisk oder der Underscore als solche angezeigt werden, statt als Syntax interpretiert zu werden, können Sie einen Backslash davorsetzen. Das Asterisk \* hier wird dann einfach als solches angezeigt.


## Listen

### Ungeordnete Listen

Hier folgt eine Liste mit Asterisk `*`.

* Erster Listeneintrag
* Zweiter Listeneintrag

Alternativ kann man auch hier den einfachen Spiegelstrich `-`verwenden.

- Noch ein Listeneintrag
- Noch noch ein Listeneintrag
+ Sogar mit einem `+` geht es


### Geordnete Listen

Geordnete Listen können durch Nummerierung angelegt werden. Die Zählung ist automatisch. Auch Untergeordnete Zählungen sind natürlich möglich durch Einrückung mit vier Leerzeichen.

1. Erster Listeneintrag
1. Zweiter Listeneintrag
    1. Ein Untereintrag
    1. Noch ein Untereintrag
1. Dritter Listeneintrag

Die Zählung ist automatisch, beginnt aber immer mit der Zahl, die im ersten Listeneintrag steht.


## Blockzitate

Mit einer einfachen schließenden, spitzen Klammer markiert man Blockzitate.

>Das hier ist ein Blockzitat. Das hier ist ein Blockzitat. Das hier ist ein Blockzitat. Das hier ist ein Blockzitat. Das hier ist ein Blockzitat. Das hier ist ein Blockzitat. Das hier ist ein Blockzitat. Das hier ist ein Blockzitat.


## Links

Links werden in Markdown besonders gut unterstützt. Im einfachsten Fall haben sie eine ganz einfache Syntax, denn Sie müssen einfach nur den Link angeben: https://wikipedia.org.

Wenn auf einem oder mehreren Wörtern ein bestimmter Link liegen soll, dann gibt es dafür allerdings eine spezielle Syntax: `[]()`.

Hier wird beispielsweise ebenfalls auf die [deutsche Wikipedia](https://de.wikipedia.org) verwiesen.

Optional können Sie auch noch einen Linktitel angeben, der als Mouseover gezeigt wird. Hier geht es also noch einmal zur [deutschen Wikipedia](https://de.wikipedia.org "Hier entlang!").

Für besonders lange Links können Sie auch mit einer Verweisstruktur arbeiten. Die Referenz im [Text][1] ist dann ganz kurz, der eigentliche Link steht an beliebiger anderer Stelle im Dokument, beispielsweise am Ende des Absatzes oder des Textes. Hier wird dann für den Identifier ein Link angegeben, wobei diese Nennung selbst nicht angezeigt wird.  

[1]: https://de.wikipedia.org


# Einige weitere Syntax-Elemente


## Code-Listings

Wenn man Code als solchen anzeigen möchte, kann man das entweder mit einzelnen Backticks im Text machen, oder mit drei Backticks auf einer Zeile.

Die Bedeutung des Elements `<head>` ist "header", also "Überschrift". Hier folgt nun ein Codeblock. Das Syntax-Highlighting ändert sich je nachdem, was man angibt. Typische Werte wären `python`, `java`, `json` oder `xml`.

```python
def open_file(filename):
    with open(filename, "r", encoding="utf8") as infile:
    content = infile.read()
    return content
```

Alternativ kann man Code auch durch Einrückung mit vier Leerzeichen als solchen markieren.

    def open_file(filename):
        with open(filename, "r", encoding="utf8") as infile:
        content = infile.read()
        return content


## Bilder

`![]()`

![Alternativtext, der für die Bildunterschrift verwendet wird](img/wikidata-logo.png "Titel des Bildes (Mouseover)")

Eine Definition der Darstellungsgröße ist aber nicht möglich. Dafür muss man das Bild dann doch über HTML einfügen, was aber auch kein Problem ist. Hier also das Bild nochmal in klein.

<img src="img/wikidata-logo.png" width="100px"/>


## Tabellen

 Tabellen sind nicht Teil der ursprünglichen Markdown-Syntax. Bitte beachten, dass hier die Ausrichtung des Textes in der zweiten Zeile mit den Doppelpunkten gesteuert wird.

| Rad      |  Farbe  | Preis   |
|:---------|:-------:|--------:|
| Mountain Bike | rot oder grün | 325,00€ |
| Rennrad | blau oder schwarz | 275,00€ |

Wie vieles andere auch kann die Darstellung der Tabelle mit CSS gesteuert werden.


## Fußnoten (pandoc)

Auch Fußnoten kennt das Original-Markdown nicht. Bei Pandoc werden Fußnoten so wie hier gezeigt umgesetzt^[Das hier ist der Fußnotentext]. Leider kann das nicht in allen Preview-Szenarien korrekt dargestellt werden.


## Formeln (pandoc)

Auch Formeln kann das Original-Markdown nicht korrekt darstellen. Pandoc erlaubt es zwar, LaTeX-Formeln einzubinden, konvertiert sie dann aber nur nach LaTeX korrekt, nicht nach HTML oder andere Formate.

Klappt das? (einfache Formel mit `$`): $E = m c ^2$

Oder das? (komplexere Formel): $c = \sqrt{ a ^2 + b ^2}$

Oder das? (einfache Formel mit LaTeX-Tag): \fbox{E = m c ^2}

Oder das? (Einbettung mit LaTeX-Tag): \fbox{c = \sqrt{ a ^2 + b ^2}}

Auch das wird nun nicht in allen Preview-Szenarien korrekt dargestellt.


## Bibliographische Angaben (pandoc)

Auch bibliographische Referenzen beherrscht das Original-Markdown nicht. Für die Transformation mit pandoc kann man aber Referenzen in eckigen Klammern und mit einem `@` verwenden, die dann auf einen Identifier in einer BibTex-Datei verweisen müssen [@burke_social_2012]. Das klappt aber erst im vollwertigen pandoc-Szenario.


Das war eigentlich das Wesentliche der Markdown-Syntax!
