$(document).ready(function() {
    $("#calendar").fullCalendar({
        googleCalendarApiKey: "AIzaSyD-mJjjbQ54nLu24mwBss6u5tRXm5Q1vKA",
        events: {
            googleCalendarId: "rnkardfkjdcc1h5mi7oqq9rip0@group.calendar.google.com",
            // eventDataTransform mutates incoming event data
            // removes names from title of events (depends on format 'reserved - name_here')
            eventDataTransform: function(eventData) {
                if (eventData.title) {
                    eventData.title = eventData.title.slice(0,eventData.title.indexOf("-")-1)
                    return eventData;
                }
            }
        }
    });
});
