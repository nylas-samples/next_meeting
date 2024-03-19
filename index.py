# Import nylas libraries
from nylas.models.auth import URLForAuthenticationConfig
from nylas.models.auth import CodeExchangeRequest
from nylas import Client
# Import FastAPI and NiceGUI libraries
from fastapi import FastAPI, Request
from nicegui import app, ui
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
# Import Date libraries
import pendulum
from datetime import datetime
# Import other libraries
import math
import os

# Import views
import views.word_clock
import views.classic
import views.led

# Initialize your Nylas client
nylas = Client(
    api_key = os.environ["V3_API_KEY"]
)

# Initialize FastAPI with a session
fastapi_app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="k33pth1ngss3cured", max_age=432000)
app.add_static_files('/static', 'static')
email_address = ""

# This is the default view
option_info = {"option":"classic"}

# Update your view
def choose_option(value):
	option_info["option"] = value

# Get the time remaining for  your next meeting in hours and minutes
def get_time(epoch):
    dt_sing = pendulum.from_timestamp(epoch)
    diff = dt_sing.diff(pendulum.now()).in_minutes()
    hours = math.trunc(diff * (1/60))
    minutes = int((diff * (1/60) - math.trunc(diff * (1/60))) * 60)
    time_tuple = (hours, minutes)
    return time_tuple

# Display how many hours and minutes are left until your next meeting
def event_display(grant, query_params, output):
	# Grab your next upcoming event
    event = nylas.events.list(grant, query_params=query_params).data
    # Grab all the elements from the view
    num_output = len(output.default_slot.children)
    # Delete all elements except the timer
    for x in range(1, num_output):
        output.remove(1)
    # Do we have an event?
    if(len(event) > 0):
		# Is the event full date or have an start and end?
        match event[0].when.object:
            case 'timespan':
                start_time = event[0].when.start_time
                time_tuple = get_time(start_time)
            case 'datespan':
                start_date = event[0].when.start_date
                date_object = datetime.strptime(start_date, "%Y-%m-%d")
                epoch_time = int(date_object.timestamp())
                time_tuple = get_time(epoch_time)
        # Here we can choose the view that we want to have
        match option_info['option']:
            case 'classic':
                views.classic.classic_view(time_tuple[0], time_tuple[1], event[0].title)
            case 'led':
                views.led.led_view(time_tuple[0], time_tuple[1], event[0].title)
            case 'word_clock':
                views.word_clock.word_clock_view(time_tuple[0], time_tuple[1], event[0].title)			    
    else:
        ui.space()
        ui.space()
        ui.space()
        with ui.grid(columns=1):
            ui.label('No meetings today ').tailwind.font_weight('black').font_size('3xl').text_color("black") 		
    
# This is our main page
@ui.page('/')
def index(request: Request):
    ui.add_head_html('<style>body {background-image: url("/static/Clocks.jpeg"); }</style>')
    with ui.column().classes('w-full items-center'):
        ui.space()
        ui.space()
        ui.space()
        ui.space()
        ui.space()
        ui.space()
        ui.space()
        ui.label('Next Meeting').tailwind.font_weight('black').font_size('5xl').text_color('black')
        ui.image('assets/Rabbit.jpeg').classes('w-64')
        # This link will take us to the login page
        with ui.link(target='/login'):
            ui.image('assets/Google.png').classes('w-64')
        ui.image('assets/PoweredBy.png').classes('w-64')

# The login page
@ui.page('/login')
def login(request: Request):
	# Session with grant
    grant = request.session.get("grant", None)
    # If there's not grant, we need to request one
    if(grant is None):
		# Send the user to the auth screen
        config = URLForAuthenticationConfig({"client_id": os.environ["V3_CLIENT"], 
                                                                      "redirect_uri" : "https://next-meeting.onrender.com/login/nylas/authorized",
                                                                      "scope":["https://www.googleapis.com/auth/calendar.events.readonly"]})
        url = nylas.auth.url_for_oauth2(config)
        response = RedirectResponse(url=url)
        return response
    else:
        # The user is logged already, let's move to the nextmeeting page 
        response = RedirectResponse(url='/nextmeeting')
        return response

# Auth page
@ui.page('/login/nylas/authorized')
def authorized(request: Request):
    code = request.query_params['code']
    # We need to exchange the code for the grant
    exchangeRequest = CodeExchangeRequest({"redirect_uri": "https://next-meeting.onrender.com/login/nylas/authorized",
                                                                              "code": code,
                                                                              "client_id": os.environ["V3_CLIENT"]})
    exchange = nylas.auth.exchange_code_for_token(exchangeRequest)
    # We get the email and the grant
    request.session["grant"] = exchange.grant_id
    request.session["email"] = exchange.email
    # Redirect to login page
    response = RedirectResponse(url='/login')
    return response

# Nextmeeting page
@ui.page('/nextmeeting')
def nextmeeting(request: Request):
    ui.add_head_html('<style>body {background-image: url("/static/Clocks.jpeg"); }</style>')
    grant = request.session.get("grant", None)
    # Make sure the user has a grant
    if(grant is None):
        response = RedirectResponse(url='/login')
        return response
    else:
		# Define the output of our page
        calendar = request.session.get("email", None)
        query_params = {"calendar_id": calendar, "limit": 1}
        with ui.column().classes('w-full items-center'):
            with ui.link(target='/logout'):
                ui.image('assets/LogOut.png').classes('w-64')
        output = ui.column().classes('w-full items-center')
        # Define a container
        with output:
			# Use a timer to repeat the same action
            ui.timer(10, lambda: event_display(grant, query_params, output))
    with ui.column().classes('w-full items-center'):
		# Radiobutton to select the view
        ui.radio(["classic", "led", "word_clock"], value="classic", on_change = lambda e: choose_option(e.value))

# Logout page
@ui.page('/logout')
def logout(request: Request):
    grant = request.session.get("grant", None)
    # Remove all sessions
    request.session.clear()
    # Destroy grant
    nylas.grants.destroy(grant)
    # Go back to main page
    response = RedirectResponse(url='/')
    return response

# Run the application
ui.run_with(fastapi_app)
