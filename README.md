# next_meeting

This is a project powered by [Nylas](https://www.nylas.com/), [FastAPI](https://fastapi.tiangolo.com/) and [NiceGUI](https://nicegui.io/).

<img width="1481" alt="next_meeting_001" src="https://github.com/nylas-samples/next_meeting/assets/1071110/12d77165-cd28-49ea-a67a-3644dd9ac916">

<img width="1480" alt="next_meeting_002" src="https://github.com/nylas-samples/next_meeting/assets/1071110/c2a57c6f-5316-4529-a2fb-a6cfda116a46">

<img width="1480" alt="next_meeting_003" src="https://github.com/nylas-samples/next_meeting/assets/1071110/0e5f5559-0aa3-4e4e-9f7c-14b15ea991e7">

<img width="1479" alt="next_meeting_004" src="https://github.com/nylas-samples/next_meeting/assets/1071110/a6fcfa49-8267-4cab-8c62-6ff4d0f5c496">

To test it locally, you need to download the repo and change some things:

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

**To make your own view follow this steps**

