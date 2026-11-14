"""Confere se cada exemplo do README casa (ou não casa) como o guia diz.

Rodar localmente com `pytest`.
"""
import re

import pytest

# (padrão, textos que devem casar, textos que não devem casar)
CASOS = [
    # Caracteres coringa e classes
    (r"a.b", ["acb", "a1b", "a b"], ["ab", "a\nb"]),
    (r"\d{3}", ["123", "2025"], ["A", "#"]),
    (r"\w+", ["alice", "_bot", "user123"], ["&", "!?"]),
    (r"Hello\sWorld", ["Hello World", "Hello\tWorld"], ["HelloWorld"]),
    # Âncoras
    (r"^Olá", ["Olá tudo"], ["Good Olá"]),
    (r"mundo!$", ["Olá, mundo!"], ["mundo! tchau"]),
    (r"\bcasa\b", ["minha casa"], ["casamento"]),
    # Conjuntos e alternância
    (r"cor[ea]ção", ["coração", "coreção"], ["coraeção"]),
    (r"[A-Za-z]", ["A", "x"], ["5", "%"]),
    (r"[^0-9]", ["b", "@"], ["1", "7"]),
    (r"sim|não", ["sim", "não"], ["talvez"]),
    # Quantificadores
    (r"ab*c", ["ac", "abc", "abbbbc"], ["adc"]),
    (r"ab+c", ["abc", "abbbc"], ["ac"]),
    (r"colou?r", ["color", "colour"], ["colouur"]),
    (r"\d{4}", ["2025"], ["123"]),
    (r"a{2,}", ["aa", "aaaaa"], ["a"]),
    (r"\d{2,4}", ["12", "1234"], ["1"]),
    # Grupos
    (r"(ha){2}", ["haha"], ["ha"]),
    (r"(?:http|https)://", ["http://", "https://"], ["ftp://"]),
    (r"(.)\1", ["aa", "11"], ["ab"]),
    # Lookahead
    (r"\d+(?= dias)", ["10 dias"], ["10 horas"]),
    (r"foo(?!bar)", ["foo123"], ["foobar"]),
    # Escape
    (r"1\+1=2", ["1+1=2"], ["11=2"]),
    # Padrões prontos
    (
        r"(?i)\bdiscord(?:app)?\.com/invite/[A-Za-z0-9-]+\b",
        ["https://discord.com/invite/abc123", "DISCORDAPP.COM/invite/xyz"],
        ["discord.com/channels/123"],
    ),
    (r"\bhttps?://\S+", ["veja https://exemplo.com"], ["exemplo.com"]),
    (
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        ["jose@exemplo.com"],
        ["a@bcom", "sem-arroba.com"],
    ),
    (r"\(?\d{2}\)?\s?9\d{4}-?\d{4}", ["(81) 99999-1234", "81999991234"], ["3333-4444"]),
    (r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", ["123.456.789-09", "12345678909"], ["123.456"]),
    (r"\d{5}-?\d{3}", ["50740-560", "50740560"], ["5074"]),
    (r"\b\d{2}/\d{2}/\d{4}\b", ["14/11/2026"], ["2026-11-14"]),
    (r"#\w+", ["#regex"], ["regex"]),
    # Padrões extras do site
    (r"\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}", ["12.345.678/0001-95", "12345678000195"], ["12.345"]),
    (r"\b\d{5}-?\d{3}\b", ["50740-560", "50740560"], ["5074"]),
    (
        r"\b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}\b",
        ["14/11/2026"],
        ["32/01/2026", "10/13/2026"],
    ),
    (r"\b[A-Z]{3}-?\d[A-Z0-9]\d{2}\b", ["ABC-1234", "ABC1D23"], ["AB-12345"]),
    (r"(?i)discord\.gg/[A-Za-z0-9-]+", ["discord.gg/abc123", "DISCORD.GG/xyz"], ["mensagem normal"]),
    (r"(?i)\bl[i1]x[o0]\b", ["lixo", "L1X0"], ["lixeira"]),
    (r"(.)\1{4,}", ["looooool"], ["lool"]),
    (
        r"(?i)(?:a{5,}|e{5,}|i{5,}|o{5,}|u{5,}|k{5,}|s{5,})",
        ["looooool", "KKKKKKK"],
        ["lool", "kkk"],
    ),
    (r"(?:<@!?\d+>[\s\S]*){5,}", ["<@1> <@2> <@3> <@!4> <@5>"], ["<@1> <@2>"]),
]


def _id(caso):
    return caso[0]


@pytest.mark.parametrize("padrao,casa,nao_casa", CASOS, ids=[_id(c) for c in CASOS])
def test_exemplo(padrao, casa, nao_casa):
    regex = re.compile(padrao)
    for texto in casa:
        assert regex.search(texto), f"{padrao!r} deveria casar com {texto!r}"
    for texto in nao_casa:
        assert not regex.search(texto), f"{padrao!r} não deveria casar com {texto!r}"


def test_lookahead_pega_so_o_numero():
    assert re.search(r"\d+(?= dias)", "10 dias").group() == "10"
