from nicegui import ui

def classic_view(hours, minutes, title) -> None:
    ui.space()
    ui.space()
    ui.space()
    with ui.grid(columns=4):
        with ui.grid(columns=1):
            ui.label(hours).tailwind.text_color("black").font_weight('bold').font_size('6xl')
        with ui.grid(columns=1):
            ui.label('')
            ui.label('Hours').tailwind.font_weight('black').font_size('4xl').text_color("black")
            ui.label('')
        with ui.grid(columns=1):
            ui.label(minutes).tailwind.text_color("black").font_weight('bold').font_size('6xl')
        with ui.grid(columns=1):
            ui.label('')
            ui.label('Minutes').tailwind.font_weight('black').font_size('4xl').text_color("black")
            ui.label('')
    with ui.grid(columns=1):
        ui.label('')
        with ui.grid(columns=2):
            ui.label('until your next meeting: ').tailwind.font_weight('black').font_size('3xl').text_color("black")
            ui.label(f'{title}').tailwind.font_weight('black').font_size('3xl').text_color("blue-700")
        ui.label('')
