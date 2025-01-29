import reflex as rx

config = rx.Config(
    app_name="Full_Stack_Reflex",
    # Connect to your own database
    db_url="postgresql://postgres:yucassql35@localhost:5432/ReflexTutorial",
    # Change the frontend port.
    frontend_port=3001,
)