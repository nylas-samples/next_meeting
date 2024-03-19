from nicegui import ui

leds = {
  0: [" _  ","| | ","|_| "],
  1: ["  ","| ","| "],
  2: [" _  "," _| ","|_  "],
  3: ["_  ","_| ","_| "],
  4: ["    ","|_| ","  | "],
  5: [" _  ","|_  "," _| "],
  6: [" _  ","|_  ","|_| "],
  7: ["_   "," |  "," |  "],
  8: [" _  ","|_| ","|_| "],
  9: [" _  ","|_| "," _| "]
}

def led_numbers(number) -> tuple[str, str]:
    i = 0
    line_1 = ""
    line_2 = ""
    line_3 = ""
    counter = 1
    while i < len(number):
         num = number[i:counter]
         i += 1
         counter += 1 
         line_1 = line_1 + leds[int(num)][0] + " "
         line_2 = line_2 + leds[int(num)][1] + " "
         line_3 = line_3 + leds[int(num)][2] + " "
    led_nums = (line_1, line_2, line_3)
    return led_nums
    
def led_view(hours, minutes, title) -> None:
    ui.space()
    ui.space()
    ui.space()
    s_hours = ""
    s_minutes = ""
    if(hours < 10):
        s_hours  = "0" + str(hours)
    else:
        s_hours = str(hours)
    if(minutes < 10):
        s_minutes  = "0" + str(minutes)
    else:
        s_minutes = str(minutes)
    t_hours = led_numbers(s_hours)
    t_minutes = led_numbers(s_minutes)

    ui.space()
    ui.space()
    ui.space()
    with ui.grid(columns=4):
        with ui.grid(columns=1):
            line = "<pre>" + t_hours[0] + "<br>" + t_hours[1] + "<br>" + t_hours[2] + "</pre>"
            ui.html(f'{line}').tailwind.text_color("black").font_weight('bold').font_size('4xl')
        with ui.grid(columns=1):
            ui.label('')
            ui.label('Hours').tailwind.font_weight('black').font_size('4xl').text_color("black")
            ui.label('')
        with ui.grid(columns=1):
            line = "<pre>" + t_minutes[0] + "<br>" + t_minutes[1] + "<br>" + t_minutes[2] + "</pre>"
            ui.html(f'{line}').tailwind.text_color("black").font_weight('bold').font_size('4xl')
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
