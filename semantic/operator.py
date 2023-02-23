from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from syntax_tree import SyntaxTree

from semantic import Semantic


class Operator(Semantic):
    # operator -> openPar expression closePar
    # operator.f = expression.f

    # operator -> num
    # operator.f = num.f

    # operator -> ident
    # operator.f -> ident.f

    def __init__(self):
        super().__init__()

    def f(self, st: SyntaxTree, n: int):
        if len(st.childNodes) == 3:
            expression: SyntaxTree = st.get_child(1)
            return expression.value.f(expression, self.UNDEFINED)
        else:
            # TODO: Fallunterscheidung ident und num
            num: SyntaxTree = st.get_child(0)
            return num.value.f(num, self.UNDEFINED)
