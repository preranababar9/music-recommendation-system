import flet as ft
from recommendation import *

def main(page):
    page.title = "Song Recommendation System" 
    
    ###creating AppBar
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.LIBRARY_MUSIC_ROUNDED),
        leading_width=40, 
        title=ft.Text("Song Recommend", size=15, italic=True),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
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
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home", selected_icon=icons.HOME_SHARP),
            ft.NavigationDestination(icon=ft.icons.SEARCH_SHARP, label="Search"),
            ft.NavigationDestination(
                icon=ft.icons.LIBRARY_BOOKS_ROUNDED,
                selected_icon=ft.icons.LIBRARY_BOOKS_SHARP,
                label="Your library",
            ),
        ]
    )


    page.add(txt_name, btn)
ft.app(target=main)