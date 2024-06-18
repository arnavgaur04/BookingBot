from Booking.booking import Booking

with Booking() as bot:
    bot.landing_page()
    bot.dismiss_popup()
    bot.destination()
    bot.date()
    bot.submit_button()
    bot.dismiss_popup()
    bot.getData()