from shiny import render, ui
from shiny.express import input

ui.panel_title("Hello Shiny!")
ui.input_slider("val", "N을 입력해주세요!",
                 0, 100, 20)
ui.input_selectize(
    "opt_val", "원하는 옵션을 선택해주세요.",
    choices=["옵션 1", "옵션 2", "옵션 3"]
)
ui.input_selectize(
    "var", "Select variable",
    choices=["bill_length_mm", "body_mass_g"]
)

@render.text
def txt():
    return f"입력받는 숫자의 2배는 {input.val() * 2} 입니다."

@render.text
def txt2():
    return f"입력하신 옵션: {input.opt_val()} 입니다."

@render.plot
def hist():
    from matplotlib import pyplot as plt
    from palmerpenguins import load_penguins
    df = load_penguins()
    df[input.var()].hist(grid=False)
    plt.xlabel(input.var())
    plt.ylabel("count")



