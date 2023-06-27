import flet as ft
from recommendation import *

def main(page):
    page.title = "Song Recommendation System" 
    
    ###creating AppBar
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.LIBRARY_MUSIC_OUTLINED),
        leading_width=40, 
        title=ft.Text("Song Recommend", size=18, italic=True),
        center_title=False,
        bgcolor=ft.colors.LIGHT_BLUE_ACCENT,
        actions=[
            ft.IconButton(ft.icons.NOTIFICATIONS_NONE),
            ft.IconButton(ft.icons.PLAY_CIRCLE),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    
    
    # event for calling function on click
    def btn_click(e):
        ###storing input value in varible
        name = txt_name.value
        ###Callling recommend function with parameter as song name taken as input from user
        try:
            print(name)
            recommend(name, page)
            
        except:
            print("error")
        # page.clean()

    ###Creating Input Field for Song Name
    txt_name = ft.TextField(label="Enter Your Favorite Song Name : " )
    
    ###creating a button for "search recommendation"
    btn = ft.ElevatedButton("GET SIMILAR SONGS", on_click=btn_click)

    ###creating a navigation bar
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_FILLED, label="Home", selected_icon=icons.HOME_FILLED),
            ft.NavigationDestination(icon=ft.icons.SEARCH_ROUNDED, label="Search"),
            ft.NavigationDestination(
                icon=ft.icons.MY_LIBRARY_MUSIC,
                selected_icon=ft.icons.MY_LIBRARY_MUSIC,
                label="Your library",
            ),
        ]
    )


    page.add(txt_name, btn)
ft.app(target=main)
