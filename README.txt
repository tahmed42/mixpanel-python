mixpanel-python
===============
This is a modified version of the official Mixpanel Python library.

This modification allows for events with a time more than 5 naive 24 hr periods
in the past to utilize Mixpanel's import endpoint instead of their track
endpoint. The track endpoint is not supported for events more than 5 days in
the past.

Getting Started
---------------
Typical usage usually looks like this:

    #!/usr/bin/env python
    from mixpanel import Mixpanel

    mp = Mixpanel(YOUR_TOKEN)

    # tracks an event with certain properties as usual
    mp.track('distinct_id', 'button clicked',
             {'color' : 'blue', 'size': 'large'})

    # track an event and import if necessary (further than 5 days in past)
    mp.track('distinct_id', 'button clicked', {'time': 1388534400},
             import_older=True)
