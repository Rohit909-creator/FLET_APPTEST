import flet as ft

def main(page: ft.page):

    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    
    def chat(p):
        text.value = textField.value
        page.update()
    page.window_width = 500
    page.window_height = 500
    # page.bgcolor = 'black'
    textField = ft.TextField(width=350)
    chatbtn = ft.ElevatedButton(text='Send',on_click=chat)

    
    container1 = ft.Container(
        margin=10,
        # padding=10,
        width=400,
        bgcolor='black',
        border_radius=35,
        content=textField
        )
    chatcontainer = ft.Container(content=chatbtn,margin=30)
    # entriesrow = ft.Row(controls=[container1])
    page.add(container1)
    page.add(chatcontainer)

    text = ft.Text(value="Test")
    container2 = ft.Container(
        margin=30,
        padding=10,
        width=400,
        height=200,
        bgcolor='black',
        border_radius=35,
        content=text
        )
    page.add(container2)
    # ft.TextStyle()
ft.app(target=main)