from nicegui import ui

def word_clock_view(hours, minutes, title) -> None:
    off_color = 'black'
    on_color = 'red'

    # hours
    ten_color = off_color
    twenty_color = off_color
    one_color = off_color
    two_color = off_color
    three_color = off_color
    four_color = off_color
    five_color = off_color
    six_color = off_color
    seven_color = off_color
    eight_color = off_color
    nine_color = off_color
    zero_color = off_color

    # minutes
    ten_min_color = off_color
    twenty_min_color = off_color
    thirty_min_color = off_color
    forty_min_color = off_color
    fifty_min_color = off_color
    one_min_color = off_color
    two_min_color = off_color
    three_min_color = off_color
    four_min_color = off_color
    five_min_color = off_color
    six_min_color = off_color
    seven_min_color = off_color
    eight_min_color = off_color
    nine_min_color = off_color
    zero_min_color = off_color

    # hours 
    if hours >= 10 and hours < 20:
        ten_color = on_color
        hours -= 10
    elif hours >= 20:
        twenty_color = on_color
        hours -= 20

    if hours < 10:
        match hours:
            case 1:
               one_color = on_color
            case 2:
               two_color = on_color
            case 3:
                three_color = on_color
            case 4:
                four_color = on_color
            case 5:
                five_color = on_color
            case 6:
                six_color = on_color
            case 7:
                seven_color = on_color
            case 8:
                eight_color = on_color
            case 9:
                nine_color = on_color
            case 0:
                zero_color = on_color

    # minutes
    if minutes >= 10 and minutes < 20:
        ten_min_color = on_color
        minutes -= 10
    elif minutes >= 20 and minutes < 30:
        twenty_min_color = on_color
        minutes -= 20
    elif minutes >= 30 and minutes < 40:
        thirty_min_color = on_color
        minutes -= 30
    elif minutes >= 40 and minutes < 50:
        forty_min_color = on_color
        minutes -= 40
    elif minutes >= 50 and minutes < 60:
        fifty_min_color = on_color
        minutes -= 50

    if minutes < 10:
        match minutes:
            case 1:
                one_min_color = on_color
            case 2:
                two_min_color = on_color
            case 3:
                three_min_color = on_color
            case 4:
                four_min_color = on_color
            case 5:
                five_min_color = on_color
            case 6:
                six_min_color = on_color
            case 7:
                seven_min_color = on_color
            case 8:
                eight_min_color = on_color
            case 9:
                nine_min_color = on_color
            case 0:
                zero_min_color = on_color
    
    ui.space()
    ui.space()
    ui.space()
    with ui.grid(columns=4):
        with ui.grid(columns=3):
            ui.label('Ten').tailwind.text_color(ten_color).font_weight('bold').font_size('xl')
            ui.label('Twenty').tailwind.text_color(twenty_color).font_weight('bold').font_size('xl')
            ui.label('One').tailwind.text_color(one_color).font_weight('bold').font_size('xl')
            ui.label('Two').tailwind.text_color(two_color).font_weight('bold').font_size('xl')
            ui.label('Three').tailwind.text_color(three_color).font_weight('bold').font_size('xl')
            ui.label('Four').tailwind.text_color(four_color).font_weight('bold').font_size('xl')
            ui.label('Five').tailwind.text_color(five_color).font_weight('bold').font_size('xl')
            ui.label('Six').tailwind.text_color(six_color).font_weight('bold').font_size('xl')
            ui.label('Seven').tailwind.text_color(seven_color).font_weight('bold').font_size('xl')
            ui.label('Eight').tailwind.text_color(eight_color).font_weight('bold').font_size('xl')
            ui.label('Nine').tailwind.text_color(nine_color).font_weight('bold').font_size('xl')
            ui.label('Zero').tailwind.text_color(zero_color).font_weight('bold').font_size('xl')
        with ui.grid(columns=1):
            ui.label('')
            ui.label('Hours').tailwind.font_weight('black').font_size('4xl').text_color(off_color)
            ui.label('')
        with ui.grid(columns=3):
            ui.label('Ten').tailwind.text_color(ten_min_color).font_weight('bold').font_size('xl')
            ui.label('Twenty').tailwind.text_color(twenty_min_color).font_weight('bold').font_size('xl')
            ui.label('Thirty').tailwind.text_color(thirty_min_color).font_weight('bold').font_size('xl')
            ui.label('Forty').tailwind.text_color(forty_min_color).font_weight('bold').font_size('xl')
            ui.label('Fifty').tailwind.text_color(fifty_min_color).font_weight('bold').font_size('xl')
            ui.label('One').tailwind.text_color(one_min_color).font_weight('bold').font_size('xl')
            ui.label('Two').tailwind.text_color(two_min_color).font_weight('bold').font_size('xl')
            ui.label('Three').tailwind.text_color(three_min_color).font_weight('bold').font_size('xl')
            ui.label('Four').tailwind.text_color(four_min_color).font_weight('bold').font_size('xl')
            ui.label('Five').tailwind.text_color(five_min_color).font_weight('bold').font_size('xl')
            ui.label('Six').tailwind.text_color(six_min_color).font_weight('bold').font_size('xl')
            ui.label('Seven').tailwind.text_color(seven_min_color).font_weight('bold').font_size('xl')
            ui.label('Eight').tailwind.text_color(eight_min_color).font_weight('bold').font_size('xl')
            ui.label('Nine').tailwind.text_color(nine_min_color).font_weight('bold').font_size('xl')
            ui.label('Zero').tailwind.text_color(zero_min_color).font_weight('bold').font_size('xl')
        with ui.grid(columns=1):
            ui.label('')
            ui.label('Minutes').tailwind.font_weight('black').font_size('4xl').text_color(off_color)
            ui.label('')
    with ui.grid(columns=1):
        ui.label('')
        with ui.grid(columns=2):
            ui.label('until your next meeting: ').tailwind.font_weight('black').font_size('3xl').text_color(off_color)
            ui.label(f'{title}').tailwind.font_weight('black').font_size('3xl').text_color("blue-700")
        ui.label('')
