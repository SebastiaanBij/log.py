# effect
## **Class:** Effect
A collection of ANSI effects in the Python format.

---

### **Attribute: ** reset
Reset ANSI effect.
??? abstract "Source"
    ````python
    reset = "\033[0m"
    ````

??? example
    ````python
    from logpy.ansi import Effect

    Effect.reset
    ````
---
### **Attribute: ** bold
Bold ANSI effect.
??? abstract "Source"
    ````python
    bold = "\033[01m"
    ````

??? example
    ````python
    from logpy.ansi import Effect

    Effect.bold
    ````
---
### **Attribute: ** disable
Disable ANSI effect.
??? abstract "Source"
    ````python
    disable = "\033[02m"
    ````

??? example
    ````python
    from logpy.ansi import Effect

    Effect.disable
    ````
---
### **Attribute: ** underline
Underline ANSI effect.
??? abstract "Source"
    ````python
    underline = "\033[04m"
    ````

??? example
    ````python
    from logpy.ansi import Effect

    Effect.underline
    ````
---
### **Attribute: ** reverse
Reverse ANSI effect.
??? abstract "Source"
    ````python
    reverse = "\033[07m"
    ````

??? example
    ````python
    from logpy.ansi import Effect

    Effect.reverse
    ````
---
### **Attribute: ** strikethrough
Strikethrough ANSI effect.
??? abstract "Source"
    ````python
    strikethrough = "\033[09m"
    ````

??? example
    ````python
    from logpy.ansi import Effect

    Effect.strikethrough
    ````
---
### **Attribute: ** invisible
Invisible ANSI effect.
??? abstract "Source"
    ````python
    invisible = "\033[08m"
    ````

??? example
    ````python
    from logpy.ansi import Effect

    Effect.invisible
    ````
---
