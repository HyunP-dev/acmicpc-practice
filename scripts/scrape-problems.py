from __future__ import annotations
from typing import NamedTuple

import requests
from bs4 import BeautifulSoup


def safe_getter(bs: BeautifulSoup, selector: str) -> str:
    if node := bs.select_one(selector):
        return node.text.strip()
    return ""


class Problem(NamedTuple):
    id: int
    title: str
    description: str
    input: str
    output: str

    @staticmethod
    def of(id: int) -> Problem:
        html = requests.get(
            "https://www.acmicpc.net/problem/" + str(id),
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
        ).text
        bs = BeautifulSoup(html, "html5lib")
        title = safe_getter(bs, "#problem_title")
        description = safe_getter(bs, "#problem_description")
        input = safe_getter(bs, "#problem_input")
        output = safe_getter(bs, "#problem_output")
        return Problem(id, title, description, input, output)
