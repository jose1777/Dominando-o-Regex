<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0f2027,50:203a43,100:2c5364&height=160&section=header&text=Dominando%20o%20Regex&fontSize=48&fontColor=ffffff&fontAlignY=45&desc=Guia%20pr%C3%A1tico%20de%20express%C3%B5es%20regulares%20em%20portugu%C3%AAs&descAlignY=72&descSize=16" />

![Idioma](https://img.shields.io/badge/idioma-PT--BR-2c5364?style=flat-square)
![Nível](https://img.shields.io/badge/n%C3%ADvel-iniciante%20ao%20intermedi%C3%A1rio-203a43?style=flat-square)
[![Teste no regex101](https://img.shields.io/badge/teste%20no-regex101-36BCF7?style=flat-square)](https://regex101.com/)
[![Testes](https://github.com/Jose1777/Dominando-o-Regex/actions/workflows/testes.yml/badge.svg)](https://github.com/Jose1777/Dominando-o-Regex/actions/workflows/testes.yml)

Cada símbolo com o que ele faz, exemplos de padrão e o que casa e não casa.<br/>
No fim tem padrões prontos e as diferenças entre Python, JavaScript e o AutoMod do Discord.<br/>
Todos os exemplos são conferidos automaticamente por testes.

</div>

---

## 📑 Sumário

- [Caracteres coringa e classes](#-caracteres-coringa-e-classes)
- [Âncoras](#-âncoras)
- [Conjuntos e alternância](#-conjuntos-e-alternância)
- [Quantificadores](#-quantificadores)
- [Grupos](#-grupos)
- [Lookahead](#-lookahead)
- [Escape](#-escape)
- [Padrões prontos](#-padrões-prontos)
- [Sabores de regex](#-sabores-de-regex)
- [Como testar](#-como-testar)
- [Testes automáticos](#-testes-automáticos)

---

## 🔤 Caracteres coringa e classes

| Símbolo | O que faz | Exemplo | ✅ Casa | ❌ Não casa |
|:-:|---|---|---|---|
| `.` | Qualquer caractere, exceto quebra de linha | `a.b` | `acb` `a1b` `a b` | `ab` `a\nb` |
| `\d` | Um dígito de 0 a 9 | `\d{3}` | `123` `2025` | `A` `#` |
| `\w` | Letra, dígito ou `_` ([acentos dependem da linguagem](#-sabores-de-regex)) | `\w+` | `alice` `_bot` `user123` | `&` `!?` |
| `\s` | Espaço, tabulação ou quebra de linha | `Hello\sWorld` | `Hello World` `Hello\tWorld` | `HelloWorld` |

> 💡 As versões maiúsculas fazem o contrário. `\D` é qualquer coisa que não seja dígito, `\W` qualquer coisa fora de `\w` e `\S` qualquer coisa que não seja espaço.

## ⚓ Âncoras

| Símbolo | O que faz | Exemplo | ✅ Casa | ❌ Não casa |
|:-:|---|---|---|---|
| `^` | Início do texto ou da linha | `^Olá` | `Olá tudo` | `Good Olá` |
| `$` | Fim do texto ou da linha | `mundo!$` | `Olá, mundo!` | `mundo! tchau` |
| `\b` | Borda de palavra | `\bcasa\b` | `minha casa` | `casamento` |

## 🎯 Conjuntos e alternância

| Símbolo | O que faz | Exemplo | ✅ Casa | ❌ Não casa |
|:-:|---|---|---|---|
| `[...]` | Qualquer um dos caracteres listados | `cor[ea]ção` | `coração` `coreção` | `coraeção` |
| `[a-z]` | Qualquer caractere do intervalo | `[A-Za-z]` | `A` `x` | `5` `%` |
| `[^...]` | Qualquer caractere fora da lista | `[^0-9]` | `b` `@` | `1` `7` |
| `\|` | "Ou" lógico entre opções | `sim\|não` | `sim` `não` | `talvez` |

## 🔁 Quantificadores

| Símbolo | O que faz | Exemplo | ✅ Casa | ❌ Não casa |
|:-:|---|---|---|---|
| `*` | Zero ou mais vezes | `ab*c` | `ac` `abc` `abbbbc` | `adc` |
| `+` | Uma ou mais vezes | `ab+c` | `abc` `abbbc` | `ac` |
| `?` | Zero ou uma vez (opcional) | `colou?r` | `color` `colour` | `colouur` |
| `{n}` | Exatamente n vezes | `\d{4}` | `2025` | `123` |
| `{n,}` | Pelo menos n vezes | `a{2,}` | `aa` `aaaaa` | `a` |
| `{n,m}` | Entre n e m vezes | `\d{2,4}` | `12` `1234` | `1` |

> 💡 Por padrão os quantificadores são **gulosos** e pegam o máximo possível. Colocando `?` depois (`*?`, `+?`) eles passam a pegar o mínimo.

## 📦 Grupos

| Símbolo | O que faz | Exemplo | ✅ Casa |
|:-:|---|---|---|
| `(...)` | Agrupa e guarda o trecho para usar depois | `(ha){2}` | `haha` |
| `(?:...)` | Agrupa sem guardar, só para organizar | `(?:http\|https)://` | `http://` `https://` |
| `\1` | Repete o que o grupo 1 capturou | `(.)\1` | `aa` `11` |

## 👀 Lookahead

| Símbolo | O que faz | Exemplo | ✅ Casa | ❌ Não casa |
|:-:|---|---|---|---|
| `(?=...)` | Confere o que vem depois sem consumir | `\d+(?= dias)` | `10` em `10 dias` | `10` em `10 horas` |
| `(?!...)` | Garante que o que vem depois **não** é o padrão | `foo(?!bar)` | `foo123` | `foobar` |

## 🛡️ Escape

| Símbolo | O que faz | Exemplo | ✅ Casa |
|:-:|---|---|---|
| `\` | Faz o próximo caractere especial valer como texto | `1\+1=2` | `1+1=2` |

> Caracteres que precisam de escape: `. ^ $ * + ? ( ) [ ] { } | \`

---

## 🧰 Padrões prontos

| Para quê | Padrão | AutoMod |
|---|---|:-:|
| Convite do Discord | `(?i)\bdiscord(?:app)?\.com/invite/[A-Za-z0-9-]+\b` | ✅ |
| Link HTTP/HTTPS | `\bhttps?://\S+` | ✅ |
| Email básico | `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}` | ✅ |
| Celular brasileiro | `\(?\d{2}\)?\s?9\d{4}-?\d{4}` | ✅ |
| CPF | `\d{3}\.?\d{3}\.?\d{3}-?\d{2}` | ✅ |
| CEP | `\d{5}-?\d{3}` | ✅ |
| Data dd/mm/aaaa | `\b\d{2}/\d{2}/\d{4}\b` | ✅ |
| Hashtag | `#\w+` | ✅ |
| Palavrão com variações (ex. "lixo", "l1x0") | `(?i)\bl[i1]x[o0]\b` | ✅ |
| Qualquer caractere repetido demais ("looooool") | `(.)\1{4,}` | ❌ |
| Letras repetidas demais, versão para o AutoMod | `(?i)(?:a{5,}\|e{5,}\|i{5,}\|o{5,}\|u{5,}\|k{5,}\|s{5,})` | ✅ |
| Menções em massa no Discord | `(?:<@!?\d+>[\s\S]*){5,}` | ✅ |

> ⚠️ Os padrões de CPF, CEP e telefone conferem só o **formato**, não se o número existe ou é válido.

## 🍦 Sabores de regex

Cada linguagem tem seu "sabor" de regex, e um padrão que funciona em uma pode dar erro ou se comportar diferente em outra. O AutoMod do Discord usa o sabor do **Rust**, que é o mais restrito dos três.

| Recurso | Exemplo | 🐍 Python | 🟨 JavaScript | 🛡️ AutoMod (Rust) |
|---|---|:-:|:-:|:-:|
| `\w` casa letra acentuada | `\w` em `ã` | ✅ | ❌ | ✅ |
| `\d` casa dígitos de outros alfabetos | `\d` em `٣` | ✅ | ❌ | ✅ |
| Lookahead | `a(?=b)` | ✅ | ✅ | ❌ erro |
| Lookbehind | `(?<=a)b` | ✅ | ✅ | ❌ erro |
| Referência a grupo | `(.)\1` | ✅ | ✅ | ❌ erro |
| Flag no início do padrão | `(?i)abc` | ✅ | ❌ erro, use `/abc/i` | ✅ |
| Grupo nomeado estilo Python | `(?P<nome>a)` | ✅ | ❌ erro | ✅ |
| Grupo nomeado estilo JS | `(?<nome>a)` | ❌ erro | ✅ | ✅ |
| Quantificador preguiçoso | `a.*?b` | ✅ | ✅ | ✅ |
| Mínimo omitido | `a{,3}` | ✅ | ❌ vira texto | ❌ erro |

> 🧪 Tabela conferida rodando cada exemplo em Python 3.13, Node.js 22 e na biblioteca `regex` do Rust (versão 1.13). O AutoMod pode estar numa versão diferente, então teste antes de salvar a regra.<br/>
> Para testar padrões do AutoMod, use o [Rustexp](https://rustexp.lpil.uk/) ou escolha **Rust** no regex101.

**Dicas para o AutoMod**
- Sem lookahead, lookbehind e `\1`. Quando precisar de repetição, liste as opções, como na versão para o AutoMod da tabela de padrões prontos
- Para ignorar maiúsculas, comece o padrão com `(?i)`

## 🧪 Como testar

1. Abra o [regex101.com](https://regex101.com/)
2. Cole o padrão no campo de cima e o texto de teste embaixo
3. O painel da direita explica cada pedaço do padrão

## ✅ Testes automáticos

Todos os exemplos deste guia estão em [`tests/test_exemplos.py`](tests/test_exemplos.py) e são conferidos pelo GitHub Actions a cada mudança. Se algum exemplo estiver errado, o selo no topo fica vermelho.

Para rodar na sua máquina:

```bash
pip install pytest
pytest
```

<div align="center">

---

Se este guia te ajudou, deixa uma ⭐ no repositório

</div>
