# Dominando o Regex

## Símbolos e Explicações

### `.`
**O que faz:**  
Age como um curinga que representa qualquer letra, número ou símbolo — exceto quebras de linha — permitindo encontrar padrões que tenham um caractere qualquer no lugar do ponto.

**Exemplos:**  
- `a.b`  
- `C.b`  
- `1.2`  
- `.x`

**Captura, Ex:**  
- `acb`  
- `a1b`  
- `a b`

**Não captura, Ex:**  
- `ab`  
- `a\nb`  

---

### `\d`
**O que faz:**  
Encontra exatamente qualquer dígito de 0 a 9. Use-o sempre que precisar reconhecer números dentro de um texto.

**Exemplos:**  
- `\d`  
- `\d\d`  
- `\d{3}`  
- `Ano: \d\d\d\d`

**Captura, Ex:**  
- `2025`  
- `7`  
- `123`

**Não captura, Ex:**  
- `A`  
- `#`  

---

### `\w`
**O que faz:**  
Localiza qualquer caractere “de palavra”: letras sem acento (A–Z, a–z), dígitos (0–9) e o sublinhado `_`.

**Exemplos:**  
- `\w`  
- `\w+`  
- `Usuário:\s\w+`

**Captura, Ex:**  
- `alice`  
- `_bot`  
- `user123`

**Não captura, Ex:**  
- `ã`  
- `&`  

---

### `\s`
**O que faz:**  
Reconhece espaços em branco: espaço normal, tabulação ou quebra de linha, útil para detectar onde há “buracos” entre palavras.

**Exemplos:**  
- `\s`  
- `\s+`  
- `Hello\sWorld`

**Captura, Ex:**  
- `Hello World`  
- `Hello\tWorld`

**Não captura, Ex:**  
- `HelloWorld`  

---

### `^`
**O que faz:**  
Garante que a busca comece exatamente no início do texto ou da linha, útil para checar prefixos.

**Exemplos:**  
- `^Olá`  
- `^Start`  
- `^\d`

**Captura, Ex:**  
- `Olá tudo`  
- `Start here`  
- `5 apples`

**Não captura, Ex:**  
- `Good Olá`  

---

### `$`
**O que faz:**  
Assegura que a correspondência termine no fim do texto ou da linha, útil para checar sufixos.

**Exemplos:**  
- `mundo!$`  
- `end$`  
- `\.$`

**Captura, Ex:**  
- `Olá, mundo!`  
- `The end`  
- `Hi.`

**Não captura, Ex:**  
- `mundo!!`  

---

### `[...]`
**O que faz:**  
Define um grupo de caracteres permitidos; corresponde a qualquer um dos símbolos listados dentro dos colchetes.

**Exemplos:**  
- `cor[ea]ção`  
- `[A-Za-z]`  
- `[0-9]`

**Captura, Ex:**  
- `coração`  
- `coraeção`  
- `A`  
- `5`

**Não captura, Ex:**  
- `X`  
- `%`  

---

### `[^...]`
**O que faz:**  
Grupo negado: casa com qualquer caractere **que não** esteja listado dentro dos colchetes.

**Exemplos:**  
- `[^aeiou]`  
- `[^0-9]`  
- `[^A-Z]`

**Captura, Ex:**  
- `b`  
- `1`  
- `@`

**Não captura, Ex:**  
- `a`  
- `Z`  

---

### `|`
**O que faz:**  
Funciona como um “ou” lógico, permitindo escolher entre várias opções.

**Exemplos:**  
- `sim|não`  
- `cat|dog`  
- `http|https`

**Captura, Ex:**  
- `sim`  
- `dog`  
- `https`

**Não captura, Ex:**  
- `maybe`  

---

### `*`
**O que faz:**  
Repete o elemento anterior de zero até muitas vezes (inclusive nenhuma).

**Exemplos:**  
- `ab*c`  
- `\w*`

**Captura, Ex:**  
- `ac`  
- `abc`  
- `abbbbbc`

---

### `+`
**O que faz:**  
Requer ao menos uma ocorrência do elemento anterior, mas aceita quantas quiser após isso.

**Exemplos:**  
- `ab+c`  
- `\d+`

**Captura, Ex:**  
- `abc`  
- `1234`

**Não captura, Ex:**  
- `ac`  

---

### `?`
**O que faz:**  
Torna o elemento anterior opcional: zero ou uma vez.

**Exemplos:**  
- `colou?r`  
- `Nov?ember`

**Captura, Ex:**  
- `color`  
- `colour`  
- `November`  
- `Novermber`  

---

### `{n}`
**O que faz:**  
Especifica que o elemento anterior deve aparecer exatamente _n_ vezes, nem mais, nem menos.

**Exemplos:**  
- `\d{4}`  
- `a{3}`

**Captura, Ex:**  
- `2025`  
- `aaa`

**Não captura, Ex:**  
- `123`  
- `aa`  

---

### `{n,}`
**O que faz:**  
Exige que o elemento anterior apareça pelo menos _n_ vezes, sem limite superior.

**Exemplos:**  
- `a{2,}`  
- `\d{2,}`

**Captura, Ex:**  
- `aa`  
- `12345`

**Não captura, Ex:**  
- `a`  

---

### `{n,m}`
**O que faz:**  
Determina que o elemento anterior deve ocorrer mínimo _n_ e máximo _m_ vezes.

**Exemplos:**  
- `a{1,3}`  
- `\d{2,4}`

**Captura, Ex:**  
- `a`  
- `aa`  
- `1234`

**Não captura, Ex:**  
- `aaaa`  
- `1`  

---

### `(pattern)`
**O que faz:**  
Agrupa o que está dentro dos parênteses e guarda o texto encontrado, permitindo repetir ou referenciar depois.

**Exemplos:**  
- `(ab)+`  
- `(ha){2}`

**Captura, Ex:**  
- `ab`  
- `abab`  
- `haha`  

---

### `(?:pattern)`
**O que faz:**  
Agrupa o padrão sem guardar o que encontrar, apenas organiza para aplicar quantificadores.

**Exemplos:**  
- `(?:http|https)://`

**Captura, Ex:**  
- `http://`  
- `https://`  

---

### `(?=pattern)`
**O que faz:**  
Lookahead positivo: confirma que o texto à frente bate com o padrão, mas não consome esses caracteres.

**Exemplos:**  
- `\d+(?= dias)`

**Captura, Ex:**  
- `10` em “10 dias”  

---

### `(?!pattern)`
**O que faz:**  
Lookahead negativo: garante que o texto à frente **não** seja o padrão indicado.

**Exemplos:**  
- `foo(?!bar)`

**Captura, Ex:**  
- `foo123`

**Não captura, Ex:**  
- `foobar`  

---

### `\\`
**O que faz:**  
Faz com que o próximo caractere seja interpretado literalmente, mesmo que seja especial em Regex.

**Exemplos:**  
- `1\+1=2`

**Captura, Ex:**  
- `1+1=2`  

---

## Exemplos de Combinações

- **Detectar convite Discord:**  
  ````regex
  (?i)\bdiscord(?:app)?\.com/invite/[A-Za-z0-9-]+\b

	•	Link HTTP/HTTPS:

\bhttps?://[^\s]+\b


	•	Número de telefone (formato simples):

\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b


	•	Filtrar “lixo” com variações:

(?i)\bl[i1]x[o0]\b


	•	Detectar repetição exagerada (e.g. “looooool”):

(.)\1{4,}


	•	Menções em massa:

(?:<@!?\d+>[\s\S]*){5,}


	•	Hashtags simples:

#\w+


	•	Emails básicos:

[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
