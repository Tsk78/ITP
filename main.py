import streamlit


def check(assert_condition: bool):
    if not assert_condition:
        exit()


def html(string: str, source=streamlit):
    source.html(string, unsafe_allow_javascript=True)


streamlit.title("Ticketing Machine")

#
# Days
#

ticket_type = streamlit.pills(
    label="Select the Number of Days",
    options=["1 Day", "3 Months", "6 Months", "12 Months"],
    selection_mode="single",
    required=True
)

check(ticket_type is not None)

#
# Guest Numbers
#

streamlit.divider()

col1, col2 = streamlit.columns(2)

with col1:
    adults = streamlit.number_input(
        label="Age 13+",
        min_value=0,
        max_value=100,
        value=0
    )

with col2:
    kids = streamlit.number_input(
        label="Age 3-12",
        min_value=0,
        max_value=100,
        value=0
    )

streamlit.caption("Kids aged below 3 are free of charge.")

check(adults + kids != 0)

#
# Ticket Type
#

streamlit.divider()

with streamlit.container():
    def create():
        return streamlit.columns([0.30, 0.70])

    if streamlit.session_state.get("current_ticket_type") is None:
        streamlit.session_state["current_ticket_type"] = -1

    def set_current_type(value: int):
        global current_type
        streamlit.session_state["current_ticket_type"] = value

    def create_select_button(key: str, index: int):
        with streamlit.columns([0.9, 0.1])[1]:
            streamlit.button("Select",
                             key=key,
                             on_click=lambda: set_current_type(index))

    type_normal = streamlit.container(
            border=streamlit.session_state["current_ticket_type"] == 0)
    with type_normal:
        icon, text = create()
        icon.image("assets/bus.png")
        text.markdown("""
                      # Normal Ticket

                      You get to enjoy a full experience of the theme park.
                      """)
    create_select_button(key="normal_ticket_type_select", index=0)

    streamlit.space("medium")

    type_plus = streamlit.container(
            border=streamlit.session_state["current_ticket_type"] == 1)
    with type_plus:
        icon, text = create()
        icon.image("assets/footsteps.png")
        text.markdown("""
                      # Prime Ticket

                      You get to enjoy a full experience of the theme park,
                      plus free 5 fast passes.
                      """)
    create_select_button(key="prime_ticket_type_select", index=1)

