# next_meeting

This is a project powered by [Nylas](https://www.nylas.com/), [FastAPI](https://fastapi.tiangolo.com/) and [NiceGUI](https://nicegui.io/).

## **You can try it out [here](https://next-meeting.onrender.com/)**

In this project, we use hosted authentication to generate a grant for the user logging in. This grant will be valid until the user logs off or after a 5 days has passed. No information from the user gets stored more that the email and the grant. The only access requested and used is the calendar's events. 

3 views are provided by default, with the option of creating new views.

<img width="1481" alt="next_meeting_001" src="https://github.com/nylas-samples/next_meeting/assets/1071110/12d77165-cd28-49ea-a67a-3644dd9ac916">

<img width="1480" alt="next_meeting_002" src="https://github.com/nylas-samples/next_meeting/assets/1071110/c2a57c6f-5316-4529-a2fb-a6cfda116a46">

<img width="1480" alt="next_meeting_003" src="https://github.com/nylas-samples/next_meeting/assets/1071110/0e5f5559-0aa3-4e4e-9f7c-14b15ea991e7">

<img width="1479" alt="next_meeting_004" src="https://github.com/nylas-samples/next_meeting/assets/1071110/a6fcfa49-8267-4cab-8c62-6ff4d0f5c496">

# To test it locally, you need to download the repo and change some things:

* First add dotenv to your libraries

```
from dotenv import load_dotenv
```

* Then change the following:

```
os.environ["V3_API_KEY"] to os.environ.get("V3_API_KEY")
```

* And finally change the following:

```
https://next-meeting.onrender.com/login/nylas/authorized with http://localhost:8000/login/nylas/authorized
```

Don't forget to add your call the call URI:

```
Head to the Hosted Authentication page on your dashboard, and click on Add a callback URI.

http://localhost:5000/login/nylas/authorized
```

For more details check the blog post [How to create a scheduler with Python and Taipy](https://www.nylas.com/blog/how-to-create-a-scheduler-with-python-and-taipy/)


# To make your own view follow this steps

```
create a new file, for example custom.py and add the following:

def custom_view(hours, minutes, title) -> None:
```

On **index.py** add the call to the view

```
import views.custom
```

On **event_display** add the following:

```
match option_info['option']:
    case 'custom':
        views.custom.custom_view(time_tuple[0], time_tuple[1], event[0].title)
```

On **def nextmeeting(request: Request):** add the following:

```
ui.radio(["classic", "led", "word_clock", "custom"], value="classic", on_change = lambda e: choose_option(e.value))
```

# Adding your custom view to the project

Simply, submit a PR 😊
